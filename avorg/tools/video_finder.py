import sys
from pathlib import Path


def videos_finder(source_directory: Path) -> list:
    movie_extensions = ('.avi', '.mkv', '.mp4')
    result = []
    for path in source_directory.glob('**/*'):
        if path.suffix in movie_extensions:
            result.append(path)
    return result


if __name__ == '__main__':
    # arguments by hand
    source_str = '../../target/'

    argv = sys.argv
    if len(argv) == 2:
        source_str = argv[1]

    source_path = Path(source_str)
    paths = videos_finder(source_path)
    print(paths)
