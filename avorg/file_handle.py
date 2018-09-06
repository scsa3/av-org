from pathlib import Path
from typing import Iterable, List


class FileHandle:
    result: List[Path]
    paths: Iterable[Path]
    # default_path = r'.'
    # HACK: this default_path is dev
    default_path = r'/Users/heweihan/PycharmProjects/av-org/videos'
    default_extensions = ('.avi', '.mkv', '.mp4')

    def __init__(self, path: str = default_path):
        self.directory = Path(path)
        self.get_files_path()

    def get_files_path(self):
        pattern = r'**/*'
        self.paths = list(self.directory.glob(pattern))

    def extension_filter(self, extensions: list = default_extensions):
        self.result = [path
                       for path in self.paths
                       if path.suffix in extensions]

    def av_filter(self, patterns: list = None):
        pass


if __name__ == '__main__':
    h = FileHandle()
    print(h.paths)
    h.extension_filter()
    print(h.result)
    print(len(h.result))
