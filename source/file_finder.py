from pathlib import Path
from typing import List, Union

class FileFinder:
    def __init__(self, input_path: Union[str, Path]):
        self.input_path = Path(input_path)

    def find_html_files(self) -> List[Path]:
        if self.input_path.is_file() and self.input_path.suffix == ".html":
            return [self.input_path]
        elif self.input_path.is_dir():
            return list(self.input_path.rglob("*.html"))
        else:
            return []
