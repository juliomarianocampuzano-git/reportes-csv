# Automatiza consultas SQL

Slug: `python-queries-automation`

Un proyecto mínimo que permite ejecutar consultas SQL simples en SQLite mediante un script en Python. El sistema es fácil de entender, testear y ejecutar sin dependencias externas. Ideal para principiantes que quieren practicar automatización de tareas con bases de datos pequeñas.

Este repo es un ejercicio junior de portfolio (SQL / Python / automatizacion).
No es un producto de produccion: cubre un caso feliz, trae datos de ejemplo y tests cortos.

## Stack

python, sqlite

## Como correrlo

```bash
python main.py
python -m pytest -q
```

## Features

- Ejecuta consultas SQL básicas en un archivo SQLite
- Muestra resultados en consola
- Permite usar comandos SQL simples como SELECT
- No requiere conexión a base de datos remota

## Datos de ejemplo

El archivo `data/sample.csv` alcanza para ver el flujo completo sin APIs externas.

## Limite honesto

No hay autenticacion, ni UI, ni escala. Sirve para leer el codigo de una sentada y
mostrar criterio de junior: un entry point, una tabla SQLite y tests del camino feliz.

## Publicacion

Repo: https://github.com/juliomarianocampuzano-git/python-queries-automation

Audiencia: AR/LATAM/EU/US
Nivel: junior
Dominio: SQL/Python/IA Automation

Este README se completo en el paso documentar del ciclo local. El post de LinkedIn
vive en LINKEDIN.md (espanol rioplatense, tono junior, con un limite honesto).