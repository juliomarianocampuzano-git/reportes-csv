# Registro de consolidación

Fecha: 29 de octubre de 2026.

Principal: [python-queries-automation](https://github.com/juliomarianocampuzano-git/python-queries-automation).

Se compararon los hashes Git de main.py, tests/test_main.py, requirements.txt, data/sample.csv y LICENSE: son idénticos en los once repositorios de origen y en el principal. No había código funcional diferente para fusionar. Las diferencias de bytecode generado no constituyen funcionalidades nuevas.

Se conservan los README y borradores de LinkedIn originales para mantener las ideas y su procedencia. Son documentos históricos: sus promesas, afirmaciones y textos de plantilla no describen necesariamente software terminado. No se publicaron mensajes en LinkedIn.

## Criterio de archivo

Después de preservar y verificar estos documentos, los once repositorios de origen se archivan sin borrarlos. Su historial y releases permanecen en cada repositorio. Este cambio no renombra repositorios ni implementa el siguiente paso del plan.

Las ideas de proyectos distintos se describen como trabajo pendiente en la sección de ideas recuperadas de este documento, con el destino previsto para cada una.

## Ideas recuperadas: trabajo pendiente

Este documento conserva lo útil de los repositorios consolidados. Ningún ítem de esta lista fue implementado como parte de la consolidación del 29 de octubre de 2026. El desarrollo requiere la aprobación de la siguiente etapa.

| Origen | Idea recuperada | Destino previsto | Alcance mínimo futuro |
| --- | --- | --- | --- |
| automatizacion-python-sql; python-automatizacion-simple | Automatizar un flujo de datos con Python y SQL | Este repositorio | Entrada CSV validada y reporte reproducible. |
| python-sql-automatizacion-junior; sql-python-automatizacion-junior | Material educativo de Python y SQLite | Este repositorio, documentación | Explicar carga, consultas y agrupaciones con ejercicios resueltos. |
| invoice-csv-parser | Resumen de facturas CSV | Este repositorio, caso de uso | Definir columnas de factura, validar montos y duplicados y exportar resultados con datos ficticios. |
| expense-split-sql | Reparto de gastos entre personas | [gastos-del-mes](https://github.com/juliomarianocampuzano-git/gastos-del-mes), etapa posterior | Personas, participaciones, saldos y precisión en centavos. |
| job-app-tracker | Seguimiento de postulaciones | [ofertas-para-mi](https://github.com/juliomarianocampuzano-git/ofertas-para-mi), etapa posterior | Guardar oferta, estado, fecha y notas sin duplicados. |
| habit-tracker-cli | Hábitos y rachas | En pausa | Definir un alcance propio antes de retomarlo. |
| rss-digest-lite | Resumen RSS/XML | En pausa | Lectura real de feeds y deduplicación antes de anunciarlo como terminado. |
| yaml-config-lint | Validación de configuración YAML | En pausa | Lectura YAML, esquema y errores claros antes de anunciarlo como terminado. |
| kebab-case-unico | Plantilla de documentación | Archivo histórico | Conservar procedencia; no mantener otro proyecto con el mismo código. |

## Estado actual del principal

Carga CSV y resumen SQL en memoria. La validación exhaustiva, persistencia en disco, exportación y funciones específicas de facturas continúan pendientes. Ver el [README](README.md) para los comandos disponibles.

## Manifiesto de procedencia

```json
{
  "date": "2026-10-29",
  "principal": "juliomarianocampuzano-git/python-queries-automation",
  "scope": "Documentación y organización; sin cambios funcionales ni borrado de repositorios.",
  "shared_files": [
    {
      "path": "main.py",
      "blob_sha": "b3801233417a33abd891021a0a40b990b8b613bf"
    },
    {
      "path": "tests/test_main.py",
      "blob_sha": "2152fda24ef4c771c065be85696a9e8ce374e96f"
    },
    {
      "path": "requirements.txt",
      "blob_sha": "2f03989dca6ec4c5072594b08f2668c750fba348"
    },
    {
      "path": "data/sample.csv",
      "blob_sha": "82f13179a67ed44392330192c3ab6e72599942ee"
    },
    {
      "path": "LICENSE",
      "blob_sha": "14fac913ccf80234b1848540089a3bbcb6e5283d"
    }
  ],
  "sources": [
    {
      "repository": "juliomarianocampuzano-git/automatizacion-python-sql",
      "source_tree_sha": "061a3fe3f767c026966876787a5423c81be689bb",
      "source_commit_sha": "061a3fe3f767c026966876787a5423c81be689bb",
      "documents": [
        {
          "original_path": "README.md",
          "blob_sha": "007601341df9dc18e4eaa092ef2fed0eb064a40a",
          "preserved_in": "CONSOLIDATION.md, sección del repositorio de origen"
        },
        {
          "original_path": "LINKEDIN.md",
          "blob_sha": "8a087f7298cd7c5ad6c25acc9e037d3686c76193",
          "preserved_in": "CONSOLIDATION.md, sección del repositorio de origen"
        }
      ]
    },
    {
      "repository": "juliomarianocampuzano-git/python-automatizacion-simple",
      "source_tree_sha": "75b4c9789654965f537005aab9f5a953c6993b39",
      "source_commit_sha": "75b4c9789654965f537005aab9f5a953c6993b39",
      "documents": [
        {
          "original_path": "README.md",
          "blob_sha": "5cc2f1a54c897da31c99cc09c4a90fee47047c50",
          "preserved_in": "CONSOLIDATION.md, sección del repositorio de origen"
        },
        {
          "original_path": "LINKEDIN.md",
          "blob_sha": "91881cf2807cbc8190a19efb2a3186296b15d718",
          "preserved_in": "CONSOLIDATION.md, sección del repositorio de origen"
        }
      ]
    },
    {
      "repository": "juliomarianocampuzano-git/python-sql-automatizacion-junior",
      "source_tree_sha": "1cdd0f6c1334642c00bfa05dc7b00d9bc9acb150",
      "source_commit_sha": "1cdd0f6c1334642c00bfa05dc7b00d9bc9acb150",
      "documents": [
        {
          "original_path": "README.md",
          "blob_sha": "53209e6ac1b4d42b847bee1b422828066924473c",
          "preserved_in": "CONSOLIDATION.md, sección del repositorio de origen"
        },
        {
          "original_path": "LINKEDIN.md",
          "blob_sha": "e429fe20722219afdf0b1434a3782a1144cdf551",
          "preserved_in": "CONSOLIDATION.md, sección del repositorio de origen"
        }
      ]
    },
    {
      "repository": "juliomarianocampuzano-git/sql-python-automatizacion-junior",
      "source_tree_sha": "35837bcf9a3dc9450531818a7cb44c1cd8c47e96",
      "source_commit_sha": "35837bcf9a3dc9450531818a7cb44c1cd8c47e96",
      "documents": [
        {
          "original_path": "README.md",
          "blob_sha": "ca1663d0f2539935c20b0be8a722d491e1a32f71",
          "preserved_in": "CONSOLIDATION.md, sección del repositorio de origen"
        },
        {
          "original_path": "LINKEDIN.md",
          "blob_sha": "0ccecb57c2e132c3b2cf766a921e1a821318a05a",
          "preserved_in": "CONSOLIDATION.md, sección del repositorio de origen"
        }
      ]
    },
    {
      "repository": "juliomarianocampuzano-git/invoice-csv-parser",
      "source_tree_sha": "739857e114a1f39e1856bf564e79baaf62710b82",
      "source_commit_sha": "739857e114a1f39e1856bf564e79baaf62710b82",
      "documents": [
        {
          "original_path": "README.md",
          "blob_sha": "d5832eda03bca72c205255c52ed2abc5830cec7d",
          "preserved_in": "CONSOLIDATION.md, sección del repositorio de origen"
        },
        {
          "original_path": "LINKEDIN.md",
          "blob_sha": "1e0f0bfeed7ec3fedbcc5597e6b5ff4cdc0ea15e",
          "preserved_in": "CONSOLIDATION.md, sección del repositorio de origen"
        }
      ]
    },
    {
      "repository": "juliomarianocampuzano-git/kebab-case-unico",
      "source_tree_sha": "cc5ec03caa654cd363c6daca3bab2267139c7671",
      "source_commit_sha": "cc5ec03caa654cd363c6daca3bab2267139c7671",
      "documents": [
        {
          "original_path": "README.md",
          "blob_sha": "1ecf26594f018dfa098df9163fe1bcb6fb00a16c",
          "preserved_in": "CONSOLIDATION.md, sección del repositorio de origen"
        },
        {
          "original_path": "LINKEDIN.md",
          "blob_sha": "c356b8a3cf54967021ed5fdd7b31c228e77f91b0",
          "preserved_in": "CONSOLIDATION.md, sección del repositorio de origen"
        }
      ]
    },
    {
      "repository": "juliomarianocampuzano-git/expense-split-sql",
      "source_tree_sha": "59d076c51d07d6d408bbb65385171665faf9f9da",
      "source_commit_sha": "59d076c51d07d6d408bbb65385171665faf9f9da",
      "documents": [
        {
          "original_path": "README.md",
          "blob_sha": "9af8acc29f585b8147ce275ba19b299570d4c090",
          "preserved_in": "CONSOLIDATION.md, sección del repositorio de origen"
        },
        {
          "original_path": "LINKEDIN.md",
          "blob_sha": "37057d4651f7bc08e153c82211a9325d4806ce51",
          "preserved_in": "CONSOLIDATION.md, sección del repositorio de origen"
        }
      ]
    },
    {
      "repository": "juliomarianocampuzano-git/job-app-tracker",
      "source_tree_sha": "9eca0bc97d911157c8d2ac2bbf4fc1df074a8fb2",
      "source_commit_sha": "9eca0bc97d911157c8d2ac2bbf4fc1df074a8fb2",
      "documents": [
        {
          "original_path": "README.md",
          "blob_sha": "27ba6e40815d96afb9c3b82714e13d5cc233ac4c",
          "preserved_in": "CONSOLIDATION.md, sección del repositorio de origen"
        },
        {
          "original_path": "LINKEDIN.md",
          "blob_sha": "a5206f719e037a5264ff20e0bb868bb7b87a7a02",
          "preserved_in": "CONSOLIDATION.md, sección del repositorio de origen"
        }
      ]
    },
    {
      "repository": "juliomarianocampuzano-git/habit-tracker-cli",
      "source_tree_sha": "a6b88b65e88100f5154f75f9a0f7fda760a4adfb",
      "source_commit_sha": "a6b88b65e88100f5154f75f9a0f7fda760a4adfb",
      "documents": [
        {
          "original_path": "README.md",
          "blob_sha": "69dba1c3fd610380244a3f78ab91cc8f0562163c",
          "preserved_in": "CONSOLIDATION.md, sección del repositorio de origen"
        },
        {
          "original_path": "LINKEDIN.md",
          "blob_sha": "73889c1ec5c1b5181af90dd39368ca8eb2a6fa3e",
          "preserved_in": "CONSOLIDATION.md, sección del repositorio de origen"
        }
      ]
    },
    {
      "repository": "juliomarianocampuzano-git/rss-digest-lite",
      "source_tree_sha": "be2791dfcef8d3ef2686a6b2ea317721381f7fa5",
      "source_commit_sha": "be2791dfcef8d3ef2686a6b2ea317721381f7fa5",
      "documents": [
        {
          "original_path": "README.md",
          "blob_sha": "edce5cd2d0a1718a32c6787286612d0cbd7ce02e",
          "preserved_in": "CONSOLIDATION.md, sección del repositorio de origen"
        },
        {
          "original_path": "LINKEDIN.md",
          "blob_sha": "cfae42066a7a115972440dc4daf89647f8cbe9df",
          "preserved_in": "CONSOLIDATION.md, sección del repositorio de origen"
        }
      ]
    },
    {
      "repository": "juliomarianocampuzano-git/yaml-config-lint",
      "source_tree_sha": "a7cc225613d8db9fa7f834e2a34b23262e8b6ad3",
      "source_commit_sha": "a7cc225613d8db9fa7f834e2a34b23262e8b6ad3",
      "documents": [
        {
          "original_path": "README.md",
          "blob_sha": "c782e641835e72628916cb994a762c0920122303",
          "preserved_in": "CONSOLIDATION.md, sección del repositorio de origen"
        },
        {
          "original_path": "LINKEDIN.md",
          "blob_sha": "84df2664267ff3bbe11f38b1670b7d1ca8ba538c",
          "preserved_in": "CONSOLIDATION.md, sección del repositorio de origen"
        }
      ]
    }
  ]
}
```

## Documentos originales preservados

Cada bloque conserva el contenido original del archivo indicado. Son borradores históricos, no una declaración de funcionalidades implementadas.

### automatizacion-python-sql

Origen: https://github.com/juliomarianocampuzano-git/automatizacion-python-sql

#### README.md

`````markdown
# Automatizando tareas con Python y SQL

Slug: `automatizacion-python-sql`

Aprende a automatizar tareas con Python y SQL para desarrollar aplicaciones más eficientes

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

- CLI con --help
- Carga de datos de ejemplo
- Resumen imprimible
- Tests del caso feliz

## Datos de ejemplo

El archivo `data/sample.csv` alcanza para ver el flujo completo sin APIs externas.

## Limite honesto

No hay autenticacion, ni UI, ni escala. Sirve para leer el codigo de una sentada y
mostrar criterio de junior: un entry point, una tabla SQLite y tests del camino feliz.

## Publicacion

Repo: https://github.com/juliomarianocampuzano-git/automatizacion-python-sql

Audiencia: AR/LATAM/EU/US
Nivel: junior
Dominio: SQL/Python/IA Automation

Este README se completo en el paso documentar del ciclo local. El post de LinkedIn
vive en LINKEDIN.md (espanol rioplatense, tono junior, con un limite honesto).
`````

#### LINKEDIN.md

`````markdown
Publique un proyecto chico de Automatizando tareas con Python y SQL, pensado para practicar python, sqlite con un alcance junior. Que hace: Aprende a automatizar tareas con Python y SQL para desarrollar aplicaciones más eficientes Como lo arme: deje un entry point claro, datos de ejemplo y tests cortos. El codigo esta simple a proposito, para que se pueda revisar sin un tour guiado. Limite honesto: no escala a produccion, no cubre todos los casos ni tiene autenticacion; es un ejercicio para mostrar criterio, no magia. Lo arme para practicar consultas simples y un CLI que se pueda leer de una sentada. Deje tests del caso feliz para no Repo: https://github.com/juliomarianocampuzano-git/automatizacion-python-sql Que le cambiarias primero: tests, README o el modelo de datos? #python #sql #automatizacion
`````

### python-automatizacion-simple

Origen: https://github.com/juliomarianocampuzano-git/python-automatizacion-simple

#### README.md

`````markdown
# Automatizar tareas en Python

Slug: `python-automatizacion-simple`

Un proyecto que utiliza Python para automatizar tareas y procesos de manera eficiente

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

- CLI con --help
- Carga de datos de ejemplo
- Resumen imprimible
- Tests del caso feliz

## Datos de ejemplo

El archivo `data/sample.csv` alcanza para ver el flujo completo sin APIs externas.

## Limite honesto

No hay autenticacion, ni UI, ni escala. Sirve para leer el codigo de una sentada y
mostrar criterio de junior: un entry point, una tabla SQLite y tests del camino feliz.

## Publicacion

Repo: https://github.com/juliomarianocampuzano-git/python-automatizacion-simple

Audiencia: AR/LATAM/EU/US
Nivel: junior
Dominio: SQL/Python/IA Automation

Este README se completo en el paso documentar del ciclo local. El post de LinkedIn
vive en LINKEDIN.md (espanol rioplatense, tono junior, con un limite honesto).
`````

#### LINKEDIN.md

`````markdown
Publique un proyecto chico de Automatizar tareas en Python, pensado para practicar python, sqlite con un alcance junior. Que hace: Un proyecto que utiliza Python para automatizar tareas y procesos de manera eficiente Como lo arme: deje un entry point claro, datos de ejemplo y tests cortos. El codigo esta simple a proposito, para que se pueda revisar sin un tour guiado. Limite honesto: no escala a produccion, no cubre todos los casos ni tiene autenticacion; es un ejercicio para mostrar criterio, no magia. Lo arme para practicar consultas simples y un CLI que se pueda leer de una sentada. Deje tests del caso feliz para no romper lo Repo: https://github.com/juliomarianocampuzano-git/python-automatizacion-simple Que le cambiarias primero: tests, README o el modelo de datos? #python #sql #automatizacion
`````

### python-sql-automatizacion-junior

Origen: https://github.com/juliomarianocampuzano-git/python-sql-automatizacion-junior

#### README.md

`````markdown
# Tutoriales de automatización con Python y SQL

Slug: `python-sql-automatizacion-junior`

Este proyecto es un tutorial de automatización con Python y SQL, diseñado para principiantes. En él, aprenderás a utilizar Python y SQLite para automatizar tareas. El proyecto incluye tutoriales, ejemplos y ejercicios prácticos para ayudarte a dominar las herramientas.

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

- Automatización de tareas con Python y SQL
- Uso de SQLite para almacenar y recuperar datos
- Tutoriales y ejercicios prácticos para principiantes

## Datos de ejemplo

El archivo `data/sample.csv` alcanza para ver el flujo completo sin APIs externas.

## Limite honesto

No hay autenticacion, ni UI, ni escala. Sirve para leer el codigo de una sentada y
mostrar criterio de junior: un entry point, una tabla SQLite y tests del camino feliz.

## Publicacion

Repo: https://github.com/juliomarianocampuzano-git/python-sql-automatizacion-junior

Audiencia: AR/LATAM/EU/US
Nivel: junior
Dominio: SQL/Python/IA Automation

Este README se completo en el paso documentar del ciclo local. El post de LinkedIn
vive en LINKEDIN.md (espanol rioplatense, tono junior, con un limite honesto).
`````

#### LINKEDIN.md

`````markdown
Hola a todos,

Quería compartir con ustedes un proyecto que he estado trabajando durante un tiempo y que creo que puede ser útil para todos aquellos que buscan aprender sobre automatización con Python y SQL.

He creado un tutorial de automatización con Python y SQL, diseñado específicamente para principiantes. El proyecto incluye tutoriales, ejemplos y ejercicios prácticos para ayudar a dominar las herramientas.

Puedes encontrar más información sobre este proyecto en mi repositorio en GitHub: https://github.com/juliomarianocampuzano-git/python-sql-automatizacion-junior

Si alguien tiene experiencia en automatización y está buscando aprender más sobre este tema, estaría encantado de compartir sus conocimientos y experiencias.

¿Cuál es el objetivo principal de una automatización con Python y SQL para ustedes?

#AprendizajeTecnológico #Automatización #Python
`````

### sql-python-automatizacion-junior

Origen: https://github.com/juliomarianocampuzano-git/sql-python-automatizacion-junior

#### README.md

`````markdown
# Automatizando consultas SQL con Python

Slug: `sql-python-automatizacion-junior`

Conocer la sintaxis SQL y automatizar consultas con Python para mejorar la eficiencia y reducir la tasa de errores.

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

- CLI con --help
- Carga de datos de ejemplo
- Resumen imprimible
- Tests del caso feliz

## Datos de ejemplo

El archivo `data/sample.csv` alcanza para ver el flujo completo sin APIs externas.

## Limite honesto

No hay autenticacion, ni UI, ni escala. Sirve para leer el codigo de una sentada y
mostrar criterio de junior: un entry point, una tabla SQLite y tests del camino feliz.

## Publicacion

Repo: https://github.com/juliomarianocampuzano-git/sql-python-automatizacion-junior

Audiencia: AR/LATAM/EU/US
Nivel: junior
Dominio: SQL/Python/IA Automation

Este README se completo en el paso documentar del ciclo local. El post de LinkedIn
vive en LINKEDIN.md (espanol rioplatense, tono junior, con un limite honesto).
`````

#### LINKEDIN.md

`````markdown
Hola a todos,

Acabo de compartir en mi repositorio personal algunos ejemplos de cómo se puede automatizar el proceso de consultas SQL utilizando Python. Como desarrollador junior en la industria de la información, siempre he buscado formas de mejorar la eficiencia y reducir la tasa de errores en mis proyectos.

Para lograr esto, he aprendido y aplicado la sintaxis SQL básica y he utilizado la biblioteca Python `sqlite3` para automatizar consultas y realizar operaciones de base de datos de manera más rápida y segura.

Si estás interesado en aprender más sobre este tema, te invito a visitar mi repositorio GitHub: https://github.com/juliomarianocampuzano-git/sql-python-automatizacion-junior

¿Cuál es tu experiencia con automatización de consultas SQL? ¿Tienes alguna pregunta o sugerencia para mejorar esta implementación?
`````

### invoice-csv-parser

Origen: https://github.com/juliomarianocampuzano-git/invoice-csv-parser

#### README.md

`````markdown
# Parser de facturas CSV

Slug: `invoice-csv-parser`

Un proyecto de Python que lee facturas exportadas a CSV, valida montos y arma un resumen SQL.

Este repo es un ejercicio junior de portfolio (SQL / Python / automatizacion).
No es un producto de produccion: cubre un caso feliz, trae datos de ejemplo y tests cortos.

## Stack

python, sqlite, csv

## Como correrlo

```bash
python main.py
python -m pytest -q
```

## Features

- Lectura de archivos CSV
- Validación de montos
- Arma de resumen SQL

## Datos de ejemplo

El archivo `data/sample.csv` alcanza para ver el flujo completo sin APIs externas.

## Limite honesto

No hay autenticacion, ni UI, ni escala. Sirve para leer el codigo de una sentada y
mostrar criterio de junior: un entry point, una tabla SQLite y tests del camino feliz.

## Publicacion

Repo: https://github.com/juliomarianocampuzano-git/invoice-csv-parser

Audiencia: AR/LATAM
Nivel: junior
Dominio: SQL/Python

Este README se completo en el paso documentar del ciclo local. El post de LinkedIn
vive en LINKEDIN.md (espanol rioplatense, tono junior, con un limite honesto).
`````

#### LINKEDIN.md

`````markdown
"Hola a todos,

Quería compartir contigo nuestro último proyecto de código abierto en GitHub. El objetivo es crear un parser de facturas CSV en Python que permita leer archivos exportados en formato CSV, validar los montos y generar un resumen SQL.

El proyecto se llama "Invoice CSV Parser" y está diseñado para ayudar a los usuarios a procesar y analizar sus facturas de manera eficiente.

Puedes encontrar más información sobre el proyecto y descargarlo directamente desde nuestro repositorio GitHub: https://github.com/juliomarianocampuzano-git/invoice-csv-parser

¿Qué te parece si contribuyes al proyecto y mejoras la funcionalidad del parser?

#Python #CódigoAbierto #Desarrollo"

Nota: Se ha mantenido un tono honesto y junior, y se ha evitado el uso de palabras disruptivas o emocionales. También se ha incluido el enlace al repositorio GitHub para que los usuarios puedan acceder fácilmente al proyecto.
`````

### kebab-case-unico

Origen: https://github.com/juliomarianocampuzano-git/kebab-case-unico

#### README.md

`````markdown
# titulo corto

Slug: `kebab-case-unico`

2-4 oraciones de que hace el proyecto

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

- CLI con --help
- Carga de datos de ejemplo
- Resumen imprimible
- Tests del caso feliz

## Datos de ejemplo

El archivo `data/sample.csv` alcanza para ver el flujo completo sin APIs externas.

## Limite honesto

No hay autenticacion, ni UI, ni escala. Sirve para leer el codigo de una sentada y
mostrar criterio de junior: un entry point, una tabla SQLite y tests del camino feliz.

## Publicacion

Repo: https://github.com/juliomarianocampuzano-git/kebab-case-unico

Audiencia: AR/LATAM/EU/US
Nivel: junior
Dominio: IA Automation

Este README se completo en el paso documentar del ciclo local. El post de LinkedIn
vive en LINKEDIN.md (espanol rioplatense, tono junior, con un limite honesto).
`````

#### LINKEDIN.md

`````markdown
Publique un proyecto chico de titulo corto, pensado para practicar python, sqlite con un alcance junior. Que hace: 2-4 oraciones de que hace el proyecto Como lo arme: deje un entry point claro, datos de ejemplo y tests cortos. El codigo esta simple a proposito, para que se pueda revisar sin un tour guiado. Limite honesto: no escala a produccion, no cubre todos los casos ni tiene autenticacion; es un ejercicio para mostrar criterio, no magia. Lo arme para practicar consultas simples y un CLI que se pueda leer de una sentada. Deje tests del caso feliz para no romper lo basico cuando toco el parser. Los datos de Repo: https://github.com/juliomarianocampuzano-git/kebab-case-unico Que le cambiarias primero: tests, README o el modelo de datos? #python #opensource #automatizacion
`````

### expense-split-sql

Origen: https://github.com/juliomarianocampuzano-git/expense-split-sql

#### README.md

`````markdown
# Divisor de gastos

Slug: `expense-split-sql`

Parte gastos entre personas y calcula saldos con consultas SQL.

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

- CLI con --help
- Carga de datos de ejemplo
- Resumen imprimible
- Tests del caso feliz

## Datos de ejemplo

El archivo `data/sample.csv` alcanza para ver el flujo completo sin APIs externas.

## Limite honesto

No hay autenticacion, ni UI, ni escala. Sirve para leer el codigo de una sentada y
mostrar criterio de junior: un entry point, una tabla SQLite y tests del camino feliz.

## Publicacion

Repo: https://github.com/juliomarianocampuzano-git/expense-split-sql

Audiencia: LATAM/US
Nivel: junior
Dominio: SQL/Python

Este README se completo en el paso documentar del ciclo local. El post de LinkedIn
vive en LINKEDIN.md (espanol rioplatense, tono junior, con un limite honesto).
`````

#### LINKEDIN.md

`````markdown
Publique un proyecto chico de Divisor de gastos, pensado para practicar python, sqlite con un alcance junior. Que hace: Parte gastos entre personas y calcula saldos con consultas SQL. Como lo arme: deje un entry point claro, datos de ejemplo y tests cortos. El codigo esta simple a proposito, para que se pueda revisar sin un tour guiado. Limite honesto: no escala a produccion, no cubre todos los casos ni tiene autenticacion; es un ejercicio para mostrar criterio, no magia. Lo arme para practicar consultas simples y un CLI que se pueda leer de una sentada. Deje tests del caso feliz para no romper lo basico cuando toco el Repo: https://github.com/juliomarianocampuzano-git/expense-split-sql Que le cambiarias primero: tests, README o el modelo de datos? #python #sql #backend
`````

### job-app-tracker

Origen: https://github.com/juliomarianocampuzano-git/job-app-tracker

#### README.md

`````markdown
# Seguimiento de postulaciones

Slug: `job-app-tracker`

CLI para anotar postulaciones laborales, estados y fechas en SQLite.

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

- CLI con --help
- Carga de datos de ejemplo
- Resumen imprimible
- Tests del caso feliz

## Datos de ejemplo

El archivo `data/sample.csv` alcanza para ver el flujo completo sin APIs externas.

## Limite honesto

No hay autenticacion, ni UI, ni escala. Sirve para leer el codigo de una sentada y
mostrar criterio de junior: un entry point, una tabla SQLite y tests del camino feliz.

## Publicacion

Repo: https://github.com/juliomarianocampuzano-git/job-app-tracker

Audiencia: AR/LATAM/EU/US
Nivel: junior
Dominio: SQL/Python

Este README se completo en el paso documentar del ciclo local. El post de LinkedIn
vive en LINKEDIN.md (espanol rioplatense, tono junior, con un limite honesto).
`````

#### LINKEDIN.md

`````markdown
Publique un proyecto chico de Seguimiento de postulaciones, pensado para practicar python, sqlite con un alcance junior. Que hace: CLI para anotar postulaciones laborales, estados y fechas en SQLite. Como lo arme: deje un entry point claro, datos de ejemplo y tests cortos. El codigo esta simple a proposito, para que se pueda revisar sin un tour guiado. Limite honesto: no escala a produccion, no cubre todos los casos ni tiene autenticacion; es un ejercicio para mostrar criterio, no magia. Lo arme para practicar consultas simples y un CLI que se pueda leer de una sentada. Deje tests del caso feliz para no romper lo basico cuando toco el Repo: https://github.com/juliomarianocampuzano-git/job-app-tracker Que le cambiarias primero: tests, README o el modelo de datos? #python #sql #backend
`````

### habit-tracker-cli

Origen: https://github.com/juliomarianocampuzano-git/habit-tracker-cli

#### README.md

`````markdown
# Tracker de habitos CLI

Slug: `habit-tracker-cli`

Registra habitos diarios en SQLite y muestra una racha simple por consola.

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

- CLI con --help
- Carga de datos de ejemplo
- Resumen imprimible
- Tests del caso feliz

## Datos de ejemplo

El archivo `data/sample.csv` alcanza para ver el flujo completo sin APIs externas.

## Limite honesto

No hay autenticacion, ni UI, ni escala. Sirve para leer el codigo de una sentada y
mostrar criterio de junior: un entry point, una tabla SQLite y tests del camino feliz.

## Publicacion

Repo: https://github.com/juliomarianocampuzano-git/habit-tracker-cli

Audiencia: LATAM/EU
Nivel: junior
Dominio: SQL/Python

Este README se completo en el paso documentar del ciclo local. El post de LinkedIn
vive en LINKEDIN.md (espanol rioplatense, tono junior, con un limite honesto).
`````

#### LINKEDIN.md

`````markdown
Publique un proyecto chico de Tracker de habitos CLI, pensado para practicar python, sqlite con un alcance junior. Que hace: Registra habitos diarios en SQLite y muestra una racha simple por consola. Como lo arme: deje un entry point claro, datos de ejemplo y tests cortos. El codigo esta simple a proposito, para que se pueda revisar sin un tour guiado. Limite honesto: no escala a produccion, no cubre todos los casos ni tiene autenticacion; es un ejercicio para mostrar criterio, no magia. Lo arme para practicar consultas simples y un CLI que se pueda leer de una sentada. Deje tests del caso feliz para no romper lo basico Repo: https://github.com/juliomarianocampuzano-git/habit-tracker-cli Que le cambiarias primero: tests, README o el modelo de datos? #python #sql #backend
`````

### rss-digest-lite

Origen: https://github.com/juliomarianocampuzano-git/rss-digest-lite

#### README.md

`````markdown
# Digest RSS ligero

Slug: `rss-digest-lite`

Lee un XML RSS de ejemplo y agrupa titulos nuevos en un resumen de texto.

Este repo es un ejercicio junior de portfolio (SQL / Python / automatizacion).
No es un producto de produccion: cubre un caso feliz, trae datos de ejemplo y tests cortos.

## Stack

python, xml

## Como correrlo

```bash
python main.py
python -m pytest -q
```

## Features

- CLI con --help
- Carga de datos de ejemplo
- Resumen imprimible
- Tests del caso feliz

## Datos de ejemplo

El archivo `data/sample.csv` alcanza para ver el flujo completo sin APIs externas.

## Limite honesto

No hay autenticacion, ni UI, ni escala. Sirve para leer el codigo de una sentada y
mostrar criterio de junior: un entry point, una tabla SQLite y tests del camino feliz.

## Publicacion

Repo: https://github.com/juliomarianocampuzano-git/rss-digest-lite

Audiencia: EU/US
Nivel: junior
Dominio: Python/IA Automation

Este README se completo en el paso documentar del ciclo local. El post de LinkedIn
vive en LINKEDIN.md (espanol rioplatense, tono junior, con un limite honesto).
`````

#### LINKEDIN.md

`````markdown
Publique un proyecto chico de Digest RSS ligero, pensado para practicar python, xml con un alcance junior. Que hace: Lee un XML RSS de ejemplo y agrupa titulos nuevos en un resumen de texto. Como lo arme: deje un entry point claro, datos de ejemplo y tests cortos. El codigo esta simple a proposito, para que se pueda revisar sin un tour guiado. Limite honesto: no escala a produccion, no cubre todos los casos ni tiene autenticacion; es un ejercicio para mostrar criterio, no magia. Lo arme para practicar consultas simples y un CLI que se pueda leer de una sentada. Deje tests del caso feliz para no romper Repo: https://github.com/juliomarianocampuzano-git/rss-digest-lite Que le cambiarias primero: tests, README o el modelo de datos? #python #opensource #automatizacion
`````

### yaml-config-lint

Origen: https://github.com/juliomarianocampuzano-git/yaml-config-lint

#### README.md

`````markdown
# Linter de YAML de config

Slug: `yaml-config-lint`

Valida claves obligatorias de un YAML de automatizacion y reporta errores claros.

Este repo es un ejercicio junior de portfolio (SQL / Python / automatizacion).
No es un producto de produccion: cubre un caso feliz, trae datos de ejemplo y tests cortos.

## Stack

python

## Como correrlo

```bash
python main.py
python -m pytest -q
```

## Features

- CLI con --help
- Carga de datos de ejemplo
- Resumen imprimible
- Tests del caso feliz

## Datos de ejemplo

El archivo `data/sample.csv` alcanza para ver el flujo completo sin APIs externas.

## Limite honesto

No hay autenticacion, ni UI, ni escala. Sirve para leer el codigo de una sentada y
mostrar criterio de junior: un entry point, una tabla SQLite y tests del camino feliz.

## Publicacion

Repo: https://github.com/juliomarianocampuzano-git/yaml-config-lint

Audiencia: EU/US
Nivel: junior
Dominio: Python/IA Automation

Este README se completo en el paso documentar del ciclo local. El post de LinkedIn
vive en LINKEDIN.md (espanol rioplatense, tono junior, con un limite honesto).
`````

#### LINKEDIN.md

`````markdown
Publique un proyecto chico de Linter de YAML de config, pensado para practicar python con un alcance junior. Que hace: Valida claves obligatorias de un YAML de automatizacion y reporta errores claros. Como lo arme: deje un entry point claro, datos de ejemplo y tests cortos. El codigo esta simple a proposito, para que se pueda revisar sin un tour guiado. Limite honesto: no escala a produccion, no cubre todos los casos ni tiene autenticacion; es un ejercicio para mostrar criterio, no magia. Lo arme para practicar consultas simples y un CLI que se pueda leer de una sentada. Deje tests del caso feliz para no romper lo basico Repo: https://github.com/juliomarianocampuzano-git/yaml-config-lint Que le cambiarias primero: tests, README o el modelo de datos? #python #opensource #automatizacion
`````

