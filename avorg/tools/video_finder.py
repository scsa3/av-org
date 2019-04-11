import sys
import re
from pathlib import Path
from typing import List


def videos_finder(source_directory: Path) -> List[Path]:
    pattern = r'^[a-zA-Z]{2,5}-?[0-9]{3,5}' \
              r'\.(avi|mkv|mp4|mpg|wmv)$'
    result = []
    for path in source_directory.glob('**/*'):
        if re.search(pattern, path.name):
            result.append(path)
    return result


if __name__ == '__main__':
    # arguments by hand
    source_str = '../temp/source/'

    argv = sys.argv
    if len(argv) == 2:
        source_str = argv[1]

    source_path = Path(source_str)
    paths = videos_finder(source_path)
    for path in paths:
        print(path)
