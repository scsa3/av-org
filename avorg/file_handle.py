from pathlib import Path
from typing import Iterable, List


class FileHandle:
    result: List[Path]
    paths: Iterable[Path]

    def __init__(self, path: str = None):
        if not path:
            path = r'.'
        self.directory = Path(path)
        self.get_files_path()

    def get_files_path(self):
        pattern = r'**/*'
        self.paths = self.directory.glob(pattern)

    def extension_filter(self, extensions: list = None):
        if not extensions:
            extensions = ['.avi', '.mkv', '.mp4']
        self.result = [path for path in self.paths
                       if path.suffix in extensions]

    def av_filter(self, patterns: list = None):
        if not patterns:
            # TODO: Correct to right behavior.
            patterns = ['.avi', '.mkv', '.mp4']
        self.result = [path for path in self.paths
                       if path.suffix in patterns]


def get_files_path(directory: str = r'.') -> list:
    pattern = r'**/*'
    paths = Path(directory).glob(pattern)
    return list(paths)


def extension_filter(paths: list = [], extensions: list = []) -> list:
    return [path for path in paths
            if path.suffix in extensions]


if __name__ == '__main__':
    h = FileHandle()
    h.get_files_path()
    print(h.paths)
