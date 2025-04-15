# main.py (temporal para prueba)
from source.html_processor import HTMLProcessor

processor = HTMLProcessor("samples/Yo tengo _ Tuya.html")
images = processor.extract_images()

print("Imágenes encontradas:", images)