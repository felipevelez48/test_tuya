# source/image_encoder.py
import base64
import os

class ImageEncoder:
    def encode_image(self, image_path, verbose=False):
        try:
            with open(image_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
                return encoded_string
        except FileNotFoundError:
            if verbose:
                print(f"Error: No se pudo encontrar la imagen en '{image_path}'")
            return None
        except Exception as e:
            if verbose:
                print(f"Error al codificar la imagen '{image_path}': {e}")
            return None
