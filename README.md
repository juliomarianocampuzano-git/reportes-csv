# CSV + SQLite: automatización de resúmenes

CLI en Python que lee un CSV, carga sus filas en SQLite en memoria y muestra el total general y los totales por categoría. Este es el repositorio principal del portfolio para este ejercicio de automatización de datos.

## Funcionalidad actual

- Entrada CSV con columnas `name`, `category` y `amount`.
- Consultas SQL de suma y agrupación por categoría.
- Selección de archivo con `--data` y ayuda con `--help`.
- Datos ficticios incluidos y tests básicos.

SQLite se utiliza en memoria: los datos no se conservan al terminar. Las consultas están definidas en el código; la CLI no acepta SQL arbitrario. La ejecución utiliza la biblioteca estándar de Python.

## Uso

```bash
python main.py --help
python main.py
python main.py --data data/sample.csv
```

Salida del CSV incluido:

```text
total=14.70
food=5.50
supplies=8.00
transport=1.20
```

## Tests

En un entorno virtual, instalar pytest y ejecutar:

```bash
python -m pip install pytest
python -m pytest -q
```

## Alcance y próximos pasos

Es un ejercicio pequeño de portfolio. La validación completa de CSV y montos, la exportación de reportes y el caso específico de facturas están pendientes. No se implementaron nuevas funciones durante la consolidación documental del 29 de octubre de 2026.

## Consolidación del portfolio

Se reunieron aquí las ideas y la documentación de once repositorios con la misma implementación base. Sus documentos originales se conservan como material histórico, con sus enlaces y hashes de origen.

- [Registro de consolidación, ideas recuperadas y documentos originales](CONSOLIDATION.md).

Los documentos históricos pueden describir funcionalidades aún no implementadas; la lista de funcionalidad actual de este README es la referencia del estado del proyecto.

## Licencia

MIT. Ver [LICENSE](LICENSE).

