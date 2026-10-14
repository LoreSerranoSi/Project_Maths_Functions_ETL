# Project Maths Functions ETL

## 1. Descripción del proyecto

Este proyecto implementa un proceso ETL (Extract, Transform, Load) en Python para calcular derivadas e integrales de funciones matemáticas y almacenar los resultados en una base de datos SQLite.

El objetivo es practicar conceptos de ingeniería de datos mediante un pipeline modular, validación de entradas, manejo de errores, logging y prevención de registros duplicados.

## 2. Arquitectura

El proyecto sigue las tres etapas principales de un proceso ETL:

- **Extract:** lee las funciones matemáticas y las operaciones desde un archivo JSON y valida las entradas.
- **Transform:** calcula derivadas o integrales utilizando SymPy y controla las expresiones inválidas.
- **Load:** almacena los resultados en SQLite y evita insertar registros duplicados.

El pipeline coordina las etapas y utiliza logging para registrar la ejecución y los posibles errores.

### Flujo del proceso

JSON → Extract → Transform → Load → SQLite

## 3. Tecnologías utilizadas

- Python
- SQLite
- SymPy
- JSON
- Logging
- Git y GitHub

## 4. Estructura del proyecto

```text
Project_Maths_Functions_ETL/
├── data/
│   ├── raw/
│   │   └── input.json
│   └── etl.db
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── pipeline.py
│   └── logging_config.py
├── .gitignore
├── requirements.txt
└── README.md
```

## 5. Instalación

Clona el repositorio y entra en su directorio:

```bash
git clone <URL_DEL_REPOSITORIO>
cd Project_Maths_Functions_ETL
```

Crea y activa un entorno virtual:

```bash
python -m venv .venv
```

En Windows:

```bash
.venv\Scripts\activate
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

## 6. Uso

Coloca las funciones matemáticas y sus operaciones en `data/raw/input.json`.

Ejecuta el pipeline según el punto de entrada implementado en el proyecto.

Consulta los logs para revisar el proceso de extracción, transformación y carga. Los resultados se almacenan en la base de datos SQLite.

## 7. Validaciones y manejo de errores

El proyecto incluye:

- Validación de datos de entrada.
- Manejo controlado de errores.
- Registro de eventos mediante logging.
- Prevención de inserciones duplicadas.
- Conteo de registros insertados y duplicados.

## 8. Objetivos de aprendizaje

- Comprender la arquitectura ETL.
- Desarrollar módulos reutilizables en Python.
- Procesar datos en formato JSON.
- Integrar Python con SQLite.
- Aplicar validaciones, logging y control de errores.
- Practicar control de versiones con Git.

## 9. Próximas mejoras

- Incorporar pruebas automatizadas.
- Explorar procesamiento de datos con PySpark.
- Integrar servicios de AWS.
- Generar visualizaciones de los resultados.