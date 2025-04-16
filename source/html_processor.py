# Creamos el procesador de los archivos .html para convertir los <img> en base64
import os
import base64
import urllib.request
from html.parser import HTMLParser
from urllib.parse import urlparse
from source.image_encoder import ImageEncoder
from source.report_generator import ReportGenerator

# Del enconder recibimos el objeto, e inicializamos dos diccionarios.
class HTMLProcessor:
    def __init__(self, encoder: ImageEncoder):
        self.encoder = encoder
        self.success = {}
        self.fail = {}

    def is_remote_url(self, src: str) -> bool:
        parsed = urlparse(src)
        return parsed.scheme in ("http", "https")

# Abrimos la imagen, verificamos si el request es OK, codificamos y devolvemos el contenido.
    def encode_remote_image(self, url, verbose=False):
        try:
            with urllib.request.urlopen(url) as response:
                if response.status != 200:
                    if verbose:
                        print(f"Error al acceder {url}: status {response.status}")
                    return None, None
                data = response.read()
                content_type = response.headers.get("Content-Type", "image/png")
                encoded = base64.b64encode(data).decode("utf-8")
                return encoded, content_type
        except Exception as e:
            if verbose:
                print(f"Error al descargar imagen remota {url}: {e}")
            return None, None

# Leemos el contenido html, buscamos la etiqueta <img>, validamos si el contenido es local o remoto.
    def process_file(self, html_path: str, output_dir: str):
        self.success = {}
        self.fail = {}

        with open(html_path, "r", encoding="utf-8") as file:
            content = file.read()

        class ImgParser(HTMLParser):
            def __init__(self, outer):
                super().__init__()
                self.outer = outer
                self.modified_html = ""

            def handle_starttag(self, tag, attrs):
                original_tag = self.get_starttag_text()
                if tag.lower() == "img":
                    attrs_dict = dict(attrs)
                    src = attrs_dict.get("src", "")

                    if not src:
                        self.modified_html += original_tag
                        return

                    if self.outer.is_remote_url(src):
                        encoded, mime_type = self.outer.encode_remote_image(src)
                        if encoded:
                            data_uri = f"data:{mime_type};base64,{encoded}"
                            attrs_dict["src"] = data_uri
                            self.outer.success[src] = "Processed (remote)"
                        else:
                            self.outer.fail[src] = "Failed to encode remote image"
                    else:
                        img_path = os.path.normpath(os.path.join(os.path.dirname(html_path), src))
                        encoded = self.outer.encoder.encode_image(img_path)
                        if encoded:
                            data_uri = f"data:image/png;base64,{encoded}"
                            attrs_dict["src"] = data_uri
                            self.outer.success[src] = "Processed (local)"
                        else:
                            self.outer.fail[src] = "Failed to encode local image"

                    attr_str = " ".join(f'{k}="{v}"' for k, v in attrs_dict.items())
                    self.modified_html += f"<{tag} {attr_str}>"
                else:
                    self.modified_html += original_tag

            def handle_data(self, data):
                self.modified_html += data

            def handle_endtag(self, tag):
                self.modified_html += f"</{tag}>"

            def handle_startendtag(self, tag, attrs):
                if tag.lower() == "img":
                    attrs_dict = dict(attrs)
                    src = attrs_dict.get("src", "")

                    if self.outer.is_remote_url(src):
                        encoded, mime_type = self.outer.encode_remote_image(src)
                        if encoded:
                            data_uri = f"data:{mime_type};base64,{encoded}"
                            attrs_dict["src"] = data_uri
                            self.outer.success[src] = "Processed (remote)"
                        else:
                            self.outer.fail[src] = "Failed to encode remote image"
                    else:
                        img_path = os.path.normpath(os.path.join(os.path.dirname(html_path), src))
                        encoded = self.outer.encoder.encode_image(img_path)
                        if encoded:
                            data_uri = f"data:image/png;base64,{encoded}"
                            attrs_dict["src"] = data_uri
                            self.outer.success[src] = "Processed (local)"
                        else:
                            self.outer.fail[src] = "Failed to encode local image"

                    attr_str = " ".join(f'{k}="{v}"' for k, v in attrs_dict.items())
                    self.modified_html += f"<{tag} {attr_str} />"
                else:
                    attr_str = " ".join(f'{k}="{v}"' for k, v in attrs)
                    self.modified_html += f"<{tag} {attr_str} />"

        parser = ImgParser(self)
        parser.feed(content)

        # Guardamos los archivos de salida, si no existe la carpeta, la creamos y los guardamos, en el lugar dónde indiquemos en el main.py
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, os.path.basename(html_path))
        with open(output_path, "w", encoding="utf-8") as out_file:
            out_file.write(parser.modified_html)

        # Generamos el reporte con las imagenens procesadas o fallidas
        report_generator = ReportGenerator()
        report = report_generator.generate_report(self.success, self.fail)
        report_generator.print_report()
        return report



