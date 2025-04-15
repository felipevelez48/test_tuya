# Este código lo haremos con ayuda de html.parser

from html.parser import HTMLParser

class ImageExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.image_paths = []

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            for attr in attrs:
                if attr[0] == 'src':
                    self.image_paths.append(attr[1])

class HTMLProcessor:
    def __init__(self, html_file):
        self.html_file = html_file

    def extract_images(self):
        with open(self.html_file, 'r', encoding='utf-8') as file:
            content = file.read()

        parser = ImageExtractor()
        parser.feed(content)
        return parser.image_paths
