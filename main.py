"""Leer CSV, validar las filas y calcular totales con SQLite."""

from __future__ import annotations

import argparse
import csv
import io
import sqlite3
import sys
from contextlib import closing
from dataclasses import dataclass
from datetime import date
from decimal import Decimal, InvalidOperation
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "sample.csv"
MAX_AMOUNT = Decimal("999999999.99")


class DataError(ValueError):
    """El archivo no tiene los datos esperados."""


@dataclass(frozen=True)
class Entry:
    name: str
    category: str
    amount_cents: int


def cents(value: str, *, positive: bool = False) -> int:
    try:
        amount = Decimal(value.strip())
        if not amount.is_finite() or abs(amount) > MAX_AMOUNT:
            raise ValueError
        rounded = amount.quantize(Decimal("0.01"))
        if rounded != amount or (positive and amount <= 0):
            raise ValueError
        return int(rounded * 100)
    except (InvalidOperation, ValueError) as exc:
        rule = "positivo, " if positive else ""
        raise DataError(
            f"el monto debe ser {rule}finito, de hasta dos decimales "
            "y no superar 999999999.99 en valor absoluto"
        ) from exc


def load_rows(path: Path, *, invoices: bool = False) -> list[Entry]:
    required = (
        ["numero", "proveedor", "fecha", "categoria", "monto"]
        if invoices
        else ["name", "category", "amount"]
    )
    entries = []
    seen = set()
    try:
        with Path(path).open(encoding="utf-8-sig", newline="") as fh:
            reader = csv.DictReader(fh, strict=True)
            if reader.fieldnames is None:
                raise DataError("el archivo no tiene encabezado")
            headers = [name.strip() for name in reader.fieldnames]
            if any(not name for name in headers) or len(headers) != len(set(headers)):
                raise DataError("hay nombres de columna vacíos o repetidos")
            missing = [name for name in required if name not in headers]
            if missing:
                raise DataError("faltan columnas: " + ", ".join(missing))
            reader.fieldnames = headers
            for raw in reader:
                try:
                    if None in raw or any(value is None for value in raw.values()):
                        raise DataError("la cantidad de campos no coincide con el encabezado")
                    row = {key: value.strip() for key, value in raw.items()}
                    empty = [key for key in required if not row[key]]
                    if empty:
                        raise DataError("faltan valores en: " + ", ".join(empty))
                    if invoices:
                        value = cents(row["monto"], positive=True)
                        parsed = date.fromisoformat(row["fecha"])
                        if parsed.isoformat() != row["fecha"]:
                            raise DataError("la fecha debe tener el formato AAAA-MM-DD")
                        key = (row["proveedor"].casefold(), row["numero"].casefold())
                        if key in seen:
                            raise DataError("factura repetida para el mismo proveedor")
                        seen.add(key)
                        entry = Entry(
                            row["proveedor"] + " / " + row["numero"], row["categoria"], value
                        )
                    else:
                        entry = Entry(row["name"], row["category"], cents(row["amount"]))
                    entries.append(entry)
                except DataError as exc:
                    raise DataError(f"línea {reader.line_num}: {exc}") from exc
                except ValueError as exc:
                    raise DataError(
                        f"línea {reader.line_num}: fecha inexistente o con formato incorrecto"
                    ) from exc
    except csv.Error as exc:
        raise DataError(f"línea {reader.line_num}: CSV mal formado: {exc}") from exc
    except UnicodeError as exc:
        raise DataError("el archivo debe estar guardado en UTF-8") from exc
    return entries


def build_db(rows: list[Entry]) -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    try:
        conn.execute(
            "CREATE TABLE items (name TEXT NOT NULL, category TEXT NOT NULL, "
            "amount_cents INTEGER NOT NULL)"
        )
        conn.executemany(
            "INSERT INTO items(name, category, amount_cents) VALUES (?, ?, ?)",
            [(row.name, row.category, row.amount_cents) for row in rows],
        )
        conn.commit()
    except Exception:
        conn.close()
        raise
    return conn


def money(value: int) -> str:
    sign = "-" if value < 0 else ""
    whole, fraction = divmod(abs(value), 100)
    return f"{sign}{whole}.{fraction:02d}"


def category_totals(conn: sqlite3.Connection) -> list[tuple[str, int]]:
    return conn.execute(
        "SELECT category, SUM(amount_cents) FROM items GROUP BY category ORDER BY category"
    ).fetchall()


def summarize(conn: sqlite3.Connection) -> str:
    total = conn.execute("SELECT COALESCE(SUM(amount_cents), 0) FROM items").fetchone()[0]
    lines = [f"total={money(total)}"]
    lines.extend(f"{category}={money(amount)}" for category, amount in category_totals(conn))
    return "\n".join(lines)


def csv_safe(value: str) -> str:
    if value.startswith(("\t", "\r", "\n")) or value.lstrip().startswith(("=", "+", "-", "@")):
        return "'" + value
    return value


def export_summary(conn: sqlite3.Connection, destination: Path) -> None:
    """Crear el reporte sin sobrescribir archivos existentes."""
    destination = Path(destination)
    output = io.StringIO(newline="")
    writer = csv.writer(output)
    writer.writerow(["categoria", "total"])
    for category, amount in category_totals(conn):
        writer.writerow([csv_safe(category), money(amount)])
    with destination.open("x", encoding="utf-8-sig", newline="") as fh:
        try:
            fh.write(output.getvalue())
        except BaseException:
            fh.close()
            destination.unlink(missing_ok=True)
            raise


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Lee un CSV y muestra el total por categoría.")
    parser.add_argument("--data", type=Path, default=DATA, metavar="ARCHIVO", help="CSV de entrada")
    parser.add_argument(
        "--facturas",
        action="store_true",
        help="usar las columnas numero, proveedor, fecha, categoria y monto",
    )
    parser.add_argument(
        "--salida", type=Path, metavar="ARCHIVO", help="guardar el resumen en un CSV nuevo"
    )
    args = parser.parse_args(argv)
    try:
        entries = load_rows(args.data, invoices=args.facturas)
        with closing(build_db(entries)) as conn:
            report = summarize(conn)
            if args.salida is not None:
                export_summary(conn, args.salida)
    except FileNotFoundError as exc:
        print(f"Error: no existe el archivo o la carpeta: {exc.filename}", file=sys.stderr)
        return 1
    except FileExistsError:
        print("Error: el archivo de salida ya existe. Elegí otro nombre.", file=sys.stderr)
        return 1
    except (DataError, OSError, sqlite3.Error) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
