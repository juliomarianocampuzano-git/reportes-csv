# Reportes CSV

[![Tests y revisión de código](https://github.com/juliomarianocampuzano-git/reportes-csv/actions/workflows/ci.yml/badge.svg)](https://github.com/juliomarianocampuzano-git/reportes-csv/actions/workflows/ci.yml)

Lee un archivo CSV, revisa las filas y calcula el total por categoría con Python y SQL. El resumen se ve en la consola y se puede guardar en otro CSV.

También incluye un ejemplo de facturas con datos ficticios.

## Cómo usarlo

Necesitás Python 3.11 o posterior. Para ejecutar el programa no hace falta instalar paquetes.

```bash
python main.py
python main.py --data data/sample.csv
python main.py --data data/sample.csv --salida resumen.csv
```

Con el archivo incluido, el resultado es:

```text
total=14.70
comida=5.50
librería=8.00
transporte=1.20
```

Para ver las opciones:

```bash
python main.py --help
```

## Qué formato tiene que tener el archivo

El CSV usa coma como separador y estas columnas:

| Columna  | Contenido                |
| -------- | ------------------------ |
| name     | Nombre del movimiento    |
| category | Categoría                |
| amount   | Monto, con punto decimal |

Ejemplo:

```csv
name,category,amount
Café,comida,3.50
Subte,transporte,1.20
```

- El archivo tiene que estar en UTF-8. También acepta el encabezado que agrega Excel al guardar en UTF-8 con BOM.
- Las columnas obligatorias y sus valores no pueden estar vacíos. Puede haber columnas adicionales.
- Los montos admiten hasta dos decimales y un máximo de 999999999.99 en valor absoluto. Se puede usar cero o un monto negativo para un ajuste.
- Los importes se guardan como centavos enteros. Por ejemplo, 0.10 + 0.20 da 0.30.
- Si encuentra un problema, indica la línea y no genera el reporte.

## Probar con facturas

```bash
python main.py --data data/facturas.csv --facturas
python main.py --data data/facturas.csv --facturas --salida resumen-facturas.csv
```

Resultado del ejemplo:

```text
total=38000.50
Insumos=20000.50
Servicios=18000.00
```

Este formato usa las columnas **numero, proveedor, fecha, categoria y monto**. Las fechas tienen que existir en el calendario y estar escritas como AAAA-MM-DD. Los montos deben ser positivos.

No admite dos facturas con el mismo número y proveedor. Para esa comparación no distingue mayúsculas de minúsculas ni espacios al principio o al final. Un mismo número puede aparecer para proveedores distintos.

El ejemplo sirve para revisar un archivo y sumar sus montos. No calcula impuestos ni valida comprobantes fiscales.

## Guardar el resumen

El archivo de salida tiene una fila por categoría:

```csv
categoria,total
Insumos,20000.50
Servicios,18000.00
```

Se guarda en UTF-8 con BOM para conservar los acentos al abrirlo en una planilla. Si una categoría empieza con un signo que una planilla pueda tomar como fórmula, se agrega un apóstrofo al exportarla.

El programa no reemplaza archivos existentes. Si el nombre de salida ya está usado, te pide elegir otro. La carpeta de destino tiene que existir.

## Cómo funciona

1. Lee el archivo y revisa columnas, valores y montos.
2. Carga las filas en una base SQLite en memoria.
3. Usa consultas SQL para sumar y agrupar por categoría.
4. Muestra el resultado y, si se indicó una salida, guarda el CSV.

Las consultas están escritas en el código. La base se cierra al terminar; el CSV original queda en su lugar.

## Tests

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
python -m ruff check .
python -m ruff format --check .
```

Los tests revisan los totales exactos, archivos con errores, facturas repetidas, fechas inválidas y exportaciones. GitHub ejecuta las mismas verificaciones en Linux y Windows.

## Repositorios relacionados

Este proyecto reúne el código compartido de los repositorios de automatización que se archivaron. Las ideas recuperadas, los enlaces a los originales y lo que sigue pendiente están en [repos-archivados.md](repos-archivados.md).

## Licencia

MIT. Ver [LICENSE](LICENSE).
