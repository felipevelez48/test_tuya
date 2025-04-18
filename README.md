# Test Data Engineer TUYA  
![Logo Tuya](images/tuya.png)

1. **Procesamiento de archivos HTML:**  
   Extrae imágenes referenciadas en etiquetas `<img>` y las reemplaza por su versión codificada en Base64, generando archivos HTML modificados sin alterar los originales.

2. **Gestión de Base de Datos con SQL:**  
   Configura y prueba una base de datos SQLite a partir de archivos Excel. Se incluye un conjunto de scripts SQL y pruebas para consultar la información.

---

## Tabla de Contenidos

- [Características](#características)
- [Arquitectura y Diseño](#arquitectura-y-diseño)
- [Instalación y Uso](#instalación-y-uso)
  - [Procesador de HTML](#procesador-de-html)
  - [Ejercicios SQL](#ejercicios-sql)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Autor](#autor)

---

## Características ✨

- **Uso de librerías estándar de Python:**  
  Sin dependencias externas para el procesamiento HTML.
- **Arquitectura Modular y Orientada a Objetos:**  
  - `FileFinder`: Recorre directorios y lista archivos HTML.  
  - `HTMLProcessor`: Parsea y modifica contenido HTML.
  - `ImageEncoder`: Convierte imágenes locales en Base64.
  - `ReportGenerator`: Registra el éxito y fallo en el procesamiento.
- **Manejo robusto de errores:**  
  Registra imágenes que se han procesado exitosamente y aquellas que han fallado, generando un reporte detallado.
- **SQL y Automatización de Base de Datos:**  
  Scripts SQL para consultas complejas basadas en datos provenientes de archivos Excel.  
  *Importante:* Siempre ejecutar `setup_database.py` antes de lanzar los scripts de consulta o pruebas.

---

## Arquitectura y Diseño 🛠

El proyecto está conformado por dos elementos clave:

### 1. Procesamiento HTML
- **Objetivo:** Recorrer archivos HTML para codificar imágenes en Base64 y reemplazar la referencia en el HTML.  
- **Componentes:**
  - **FileFinder:** Encuentra archivos `.html` en el directorio especificado.
  - **HTMLProcessor:** Utiliza el parser `HTMLParser` de Python para identificar y reemplazar etiquetas `<img>`.
  - **ImageEncoder:** Lee archivos de imagen y los codifica en Base64.
  - **ReportGenerator:** Genera y muestra un reporte final con las imágenes procesadas y errores.

### 2. Gestión de Base de Datos (puntos_sql)
- **Objetivo:** Configurar y ejecutar consultas sobre una base de datos SQLite utilizando archivos Excel como fuente de datos.
- **Secuencia de Ejecución:**
  1. Ejecutar `setup_database.py` para crear la base de datos y cargar los datos originales desde `bd.xlsx` y `rachas.xlsx`.
  2. Utilizar los scripts de consultas (`ejercicio2.sql`, `ejercicio3.sql`) o ejecutar las pruebas (`test_ejercicio2.py`, `test_ejercicio3.py`, `test_tables_in_db.py`).

---

## Estructura del Proyecto

```plaintext
├── README.md
├── main.py                   # Orquestador principal del procesador HTML
├── source
│   ├── file_finder.py        # Clase para buscar archivos HTML
│   ├── html_processor.py     # Procesamiento y reemplazo de imágenes en HTML
│   ├── image_encoder.py      # Codificación de imágenes a Base64
│   └── report_generator.py   # Generación de reporte de éxito/fallo en el procesamiento
├── samples                   # Archivos HTML originales
│   ├── ejemplo1.html
│   ├── ejemplo2.html
│   ├── AWS _ Cloud Computing - Servicios de informática en la nube.html
│   ├── FINVIZ.com - Stock Screener.html
│   ├── GuruFocus _ Stock Market Research, Data and Tools.html
│   ├── Platzi_ Cursos Online de programación, AI, data science y más.html
│   ├── Yo tengo _ Tuya.html
├── images
│   └── tuya.png              # Logo o imágenes referenciales
├── output                    # Archivos HTML modificados tras la ejecución
├── .gitignore
└── puntos_sql                # Scripts y recursos para la parte SQL
    ├── data
    │   ├── bd.xlsx          # Archivo original sin modificaciones
    │   └── rachas.xlsx      # Archivo original sin modificaciones
    └── scripts
        ├── ejercicio2.sql   # Consulta SQL ejemplo 2
        ├── ejercicio3.sql   # Consulta SQL ejemplo 3
        ├── setup_database.py # Script para configurar la base de datos (ejecutar primero)
        ├── test_ejercicio2.py       # Prueba para ejercicio2.sql
        ├── test_ejercicio3.py       # Prueba para ejercicio3.sql
        └── test_tables_in_db.py    # Prueba de estructura de tablas
```
#instalación-y-uso
Instalación y Uso 🔧
## Requisitos
- **Python ≥ 3.8 instalado.**
- **(Opcional) Un entorno virtual (virtualenv, venv, etc.).**

## Procesador de HTML
Clonar el repositorio:

```bash
git clone https://github.com/felipevelez48/test_tuya.git
cd tuya_project
```
Ejecutar el procesador:

```bash
python main.py
```
Esto buscará archivos HTML en la carpeta samples, procesará las imágenes y generará los archivos modificados en output. Se mostrará un resumen en consola con estadísticas de éxito y fallos.

## Ejercicios SQL
- Configuración de la Base de Datos: Navega a la carpeta puntos_sql/scripts y ejecuta:

```bash
python setup_database.py
```
Esto creará la base de datos y cargará los datos desde los archivos Excel ubicados en puntos_sql/data.

-Ejecución de Consultas y Pruebas:

Para ejecutar las consultas manualmente, utiliza el motor SQL de tu preferencia (por ejemplo, SQLite CLI) apuntando a la base de datos generada.

Para ejecutar las pruebas:

```bash
python test_ejercicio2.py
python test_ejercicio3.py
python test_tables_in_db.py
```
# 💡 Autor 📊🤖
## John Felipe Vélez
### Data Engineer
