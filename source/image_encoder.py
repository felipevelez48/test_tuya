import base64

# definimos la clase
#recibe la ruta, devuelve la cadena en base64 y si hay error devuelve None
#Lo convertimos en str y si está malo tenemos el error.
class ImageEncoder:
    def encode_image(self, image_path: str) -> str:
        try:
            with open(image_path, "rb") as image_file:
                encoded = base64.b64encode(image_file.read()).decode("utf-8")
                return encoded
        except Exception as e:
            print(f"[ERROR] No se pudo codificar la imagen {image_path}: {e}")
            return None
