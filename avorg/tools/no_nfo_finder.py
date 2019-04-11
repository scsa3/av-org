import sys
import re
from pathlib import Path
from typing import List


def no_nfo_videos_finder(source_directory: Path) -> List[Path]:
    pattern = r'^[a-zA-Z]{2,5}-?[0-9]{3,5}' \
              r'\.(avi|mkv|mp4|mpg|wmv)$'
    result = []
    for path in source_directory.glob('**/*'):
        if re.search(pattern, path.name):
            nfo_path = Path(path.parent / (path.stem + '.nfo'))
            if not nfo_path.is_file():
                result.append(path)
    return result


if __name__ == '__main__':
    # arguments by hand
    source_str = 'T:\Porn\\Scrapied\\'
    target_str = 'T:\Porn\\temp\\'

    argv = sys.argv
    if len(argv) == 3:
        source_str, target_str = argv[1] = argv[2]

    source = Path(source_str)
    target = Path(target_str)
    no_nfo_paths = no_nfo_videos_finder(source)
    print(no_nfo_paths)


    def no_nfo_mover(paths: List[Path]) -> None:
        for path in paths:
            new_path = target / path.name
            print(new_path)
            path.rename(new_path)
