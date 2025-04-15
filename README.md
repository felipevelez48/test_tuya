# test_tuya
# Test Data Engineer TUYA
![Logo Tuya](images/tuya.png)

# Punto número uno

## Procesador de Archivos HTML a Base64 💻🌐
Este proyecto se encarga de recorrer archivos HTML para extraer imágenes referenciadas en etiquetas `<img>` y reemplazarlas con su versión codificada en base64. Así se generan nuevos archivos HTML sin modificar los originales.

## Tabla de Contenidos
- [Características](#características)
- [Arquitectura y Diseño](#arquitectura-y-diseño)
- [Instalación y Uso](#instalación-y-uso)
- [Ejemplos](#ejemplos)
- [Pruebas](#pruebas)
- [Mejoras Futuras](#mejoras-futuras)
- [Autor](#autor)

## Características ✨

- Uso exclusivo de las librerías estándar de Python.
- Implementación de dos métodos para extraer imágenes: expresiones regulares y `html.parser`.
- Programación orientada a objetos con principios SOLID.
- Manejo robusto de errores, registrando imágenes que se procesen correctamente y aquellas que fallen. Generando un objeto que contenga la lista de imágenes procesadas de forma exitosa y las que fallaron:
```plaintext
{
    success: {},
    fail: {}
} 
```
## Arquitectura y Diseño 🛠

El proyecto cuenta con las siguientes clases:
- **FileFinder:** Recorre directorios y lista los archivos HTML.
- **HTMLProcessor:** Parsea y modifica el contenido HTML.
- **ImageEncoder:** Convierte las imágenes a base64.
- **ReportGenerator:** Registra el éxito y fallo en el procesamiento.

### Estructura del Proyecto

```plaintext
├── README.md
├── source
│   ├── file_finder.py
│   ├── html_processor.py
│   ├── image_encoder.py
│   └── report_generator.py
├── samples
│   ├── ejemplo1.html
├── tests
│   └── test_processor.py
├── images
    ├── tuya.png
└── .gitignore
```

#### 4. Instalación y Uso
Explica cómo instalar las herramientas necesarias (en este caso, basta con tener Python) y cómo ejecutar el proyecto:
```markdown
## Instalación y Uso 🔧

### Requisitos
- Python 3.x instalado.

### Ejecución
Para ejecutar el proyecto, abre una terminal y ejecuta:
```bash
python src/main.py --input /ruta/a/tu/directorio_o_archivos


#### 5. Ejemplos
Incluye ejemplos de uso, fragmentos de salida o capturas de pantalla:
```markdown
## Ejemplos de Uso 📸

**Ejemplo de archivo HTML original:**
```html
<html>
  <body>
    <img src="imagenes/foto.png" alt="Descripción">
  </body>
</html>


