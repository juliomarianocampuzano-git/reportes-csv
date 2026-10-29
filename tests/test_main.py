import csv
import io
from contextlib import closing
from pathlib import Path

import pytest

import main


def make_csv(tmp_path, text, name="entrada.csv"):
    path = tmp_path / name
    path.write_text(text, encoding="utf-8")
    return path


def test_sample_report_is_exact():
    with closing(main.build_db(main.load_rows(main.DATA))) as conn:
        assert main.summarize(conn) == "total=14.70\ncomida=5.50\nlibrería=8.00\ntransporte=1.20"


def test_decimal_totals_and_negative_adjustments(tmp_path):
    path = make_csv(
        tmp_path,
        "name,category,amount\nUno,Comida,0.10\nDos,Comida,0.20\nDevolución,Comida,-0.05\n",
    )
    with closing(main.build_db(main.load_rows(path))) as conn:
        assert main.summarize(conn) == "total=0.25\nComida=0.25"


@pytest.mark.parametrize(
    "amount",
    ["NaN", "Infinity", "-Infinity", "1.001", "1e99999", "1000000000", "-1000000000", "abc", ""],
)
def test_invalid_amount_reports_the_line(tmp_path, amount):
    path = make_csv(tmp_path, f"name,category,amount\nCompra,Hogar,{amount}\n")
    with pytest.raises(main.DataError, match="línea 2"):
        main.load_rows(path)


@pytest.mark.parametrize(
    "value,cents", [("0", 0), ("-0.01", -1), ("1.2300", 123), ("999999999.99", 99999999999)]
)
def test_valid_amount_boundaries(value, cents):
    assert main.cents(value) == cents


@pytest.mark.parametrize(
    "content,message",
    [
        ("", "encabezado"),
        ("name,category\nCompra,Hogar\n", "amount"),
        ("name,category,category,amount\nCompra,Hogar,Hogar,1\n", "repetidos"),
        ("name,,amount\nCompra,Hogar,1\n", "vacíos"),
        ("name,category,amount\nCompra,Hogar,1,extra\n", "cantidad de campos"),
        ("name,category,amount\nCompra,Hogar\n", "cantidad de campos"),
        ("name,category,amount\n,Comida,1\n", "name"),
        ("name,category,amount\nCompra,,1\n", "category"),
        ('name,category,amount\n"sin cierre,Hogar,1\n', "CSV mal formado"),
    ],
)
def test_bad_csv_has_useful_errors(tmp_path, content, message):
    with pytest.raises(main.DataError, match=message):
        main.load_rows(make_csv(tmp_path, content))


def test_utf8_bom_spaces_extra_columns_and_quoted_values(tmp_path):
    path = make_csv(
        tmp_path, '\ufeff name , category , amount ,nota\n"Compra, hogar", Hogar ,1.20,Ejemplo\n'
    )
    rows = main.load_rows(path)
    assert rows == [main.Entry("Compra, hogar", "Hogar", 120)]


def test_bad_encoding_is_explained(tmp_path):
    path = tmp_path / "entrada.csv"
    path.write_bytes(b"name,category,amount\nCaf\xe9,Hogar,1\n")
    with pytest.raises(main.DataError, match="UTF-8"):
        main.load_rows(path)


def test_header_only_file_has_zero_total(tmp_path):
    path = make_csv(tmp_path, "name,category,amount\n")
    with closing(main.build_db(main.load_rows(path))) as conn:
        assert main.summarize(conn) == "total=0.00"


def test_facturas_example_totals():
    path = Path(main.ROOT) / "data" / "facturas.csv"
    with closing(main.build_db(main.load_rows(path, invoices=True))) as conn:
        assert main.summarize(conn) == "total=38000.50\nInsumos=20000.50\nServicios=18000.00"


@pytest.mark.parametrize(
    "date", ["2026-02-29", "2026-04-31", "2026-1-01", "20261003", "0000-01-01"]
)
def test_factura_dates_are_validated(tmp_path, date):
    path = make_csv(
        tmp_path, f"numero,proveedor,fecha,categoria,monto\nA-1,Proveedor,{date},Insumos,1\n"
    )
    with pytest.raises(main.DataError, match="línea 2"):
        main.load_rows(path, invoices=True)


@pytest.mark.parametrize("amount", ["0", "-1"])
def test_facturas_require_positive_amounts(tmp_path, amount):
    path = make_csv(
        tmp_path,
        f"numero,proveedor,fecha,categoria,monto\nA-1,Proveedor,2026-10-03,Insumos,{amount}\n",
    )
    with pytest.raises(main.DataError, match="positivo"):
        main.load_rows(path, invoices=True)


def test_duplicate_facturas_are_rejected_but_other_suppliers_are_allowed(tmp_path):
    header = "numero,proveedor,fecha,categoria,monto\n"
    first = "A-1,Proveedor,2026-10-03,Insumos,10\n"
    duplicate = "a-1, PROVEEDOR ,2026-10-04,Insumos,20\n"
    path = make_csv(tmp_path, header + first + duplicate)
    with pytest.raises(main.DataError, match="línea 3: factura repetida"):
        main.load_rows(path, invoices=True)
    path.write_text(header + first + "A-1,Otro proveedor,2026-10-04,Insumos,20\n", encoding="utf-8")
    assert len(main.load_rows(path, invoices=True)) == 2


def test_export_has_exact_totals_and_protects_formula_text(tmp_path):
    path = make_csv(
        tmp_path, "name,category,amount\nUno,=1+1,0.10\nDos,=1+1,0.20\nTres,Salud,2.50\n"
    )
    output = tmp_path / "resumen.csv"
    with closing(main.build_db(main.load_rows(path))) as conn:
        main.export_summary(conn, output)
    rows = list(csv.DictReader(io.StringIO(output.read_text(encoding="utf-8-sig"))))
    assert rows == [
        {"categoria": "'=1+1", "total": "0.30"},
        {"categoria": "Salud", "total": "2.50"},
    ]
    assert output.read_bytes().startswith(b"\xef\xbb\xbf")


def test_export_never_overwrites_input_or_existing_report(tmp_path, capsys):
    path = make_csv(tmp_path, "name,category,amount\nCompra,Hogar,1\n")
    original = path.read_bytes()
    assert main.main(["--data", str(path), "--salida", str(path)]) == 1
    assert path.read_bytes() == original
    assert "ya existe" in capsys.readouterr().err
    assert list(tmp_path.glob(".resumen-*")) == []


def test_failed_export_does_not_leave_a_partial_report(tmp_path, monkeypatch):
    original_open = Path.open

    class FailingWriter:
        def __init__(self, stream):
            self.stream = stream

        def __enter__(self):
            return self

        def __exit__(self, *_):
            self.stream.close()

        def close(self):
            self.stream.close()

        def write(self, text):
            self.stream.write(text[:5])
            raise OSError("No se pudo terminar de guardar")

    def failing_open(path, *args, **kwargs):
        return FailingWriter(original_open(path, *args, **kwargs))

    rows = main.load_rows(main.DATA)
    monkeypatch.setattr(Path, "open", failing_open)
    with closing(main.build_db(rows)) as conn:
        with pytest.raises(OSError):
            main.export_summary(conn, tmp_path / "resumen.csv")
    assert list(tmp_path.iterdir()) == []


def test_bad_data_does_not_create_a_partial_report(tmp_path, capsys):
    path = make_csv(tmp_path, "name,category,amount\nCompra,Hogar,1\nOtro,Hogar,NaN\n")
    output = tmp_path / "resumen.csv"
    assert main.main(["--data", str(path), "--salida", str(output)]) == 1
    captured = capsys.readouterr()
    assert captured.out == ""
    assert "línea 3" in captured.err
    assert not output.exists()


def test_missing_file_returns_a_short_error(tmp_path, capsys):
    assert main.main(["--data", str(tmp_path / "falta.csv")]) == 1
    captured = capsys.readouterr()
    assert "no existe" in captured.err
    assert "Traceback" not in captured.err


def test_cli_can_run_outside_project_directory(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    assert main.main([]) == 0
    assert capsys.readouterr().out == "total=14.70\ncomida=5.50\nlibrería=8.00\ntransporte=1.20\n"


def test_facturas_cli_and_saved_report(tmp_path, capsys):
    output = tmp_path / "facturas-resumen.csv"
    assert (
        main.main(
            [
                "--data",
                str(main.ROOT / "data" / "facturas.csv"),
                "--facturas",
                "--salida",
                str(output),
            ]
        )
        == 0
    )
    assert "total=38000.50" in capsys.readouterr().out
    assert output.read_text(encoding="utf-8-sig").splitlines() == [
        "categoria,total",
        "Insumos,20000.50",
        "Servicios,18000.00",
    ]
