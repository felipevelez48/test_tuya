# Este código lo haremos con ayuda de html.parser

import os
from html.parser import HTMLParser
from source.image_encoder import ImageEncoder
from source.report_generator import ReportGenerator

class HTMLProcessor:
    def __init__(self, encoder: ImageEncoder):
        self.encoder = encoder
        self.success = {}
        self.fail = {}

    def process_file(self, html_path: str, output_dir: str):
        with open(html_path, "r", encoding="utf-8") as file:
            content = file.read()

        # Detectamos cada etiqueta <img> y reemplazamos el src por su versión en base64
        class ImgParser(HTMLParser):
            def __init__(self, outer):
                super().__init__()
                self.outer = outer
                self.modified_html = ""
                self.last_pos = 0

            def handle_starttag(self, tag, attrs):
                if tag.lower() == "img":
                    for i, (attr, value) in enumerate(attrs):
                        if attr.lower() == "src":
                            img_path = os.path.join(os.path.dirname(html_path), value)
                            encoded = self.outer.encoder.encode_image(img_path)
                            if encoded:
                                self.outer.success[value] = "Processed"
                                base64_src = f"data:image/png;base64,{encoded}"
                            else:
                                self.outer.fail[value] = "Failed to encode"
                                base64_src = value

                            
                            attrs[i] = (attr, base64_src)

                self.modified_html += self.get_starttag_text()

            def handle_data(self, data):
                self.modified_html += data

            def handle_endtag(self, tag):
                self.modified_html += f"</{tag}>"

        # Procesamos el archivo HTML
        parser = ImgParser(self)
        parser.feed(content)

        # Guardamos el archivo procesado
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, os.path.basename(html_path))
        with open(output_path, "w", encoding="utf-8") as out_file:
            out_file.write(parser.modified_html)

        # Generamos el reporte
        report_generator = ReportGenerator()
        report = report_generator.generate_report(self.success, self.fail)
        report_generator.print_report()
        return report


