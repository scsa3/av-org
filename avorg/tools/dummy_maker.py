import sys
from pathlib import Path


def dummy_maker(source_directory: Path, target_directory: Path) -> None:
    for path in source_directory.glob('**/*'):
        new_path = target_directory / path
        if path.is_dir():
            new_path.mkdir(parents=True, exist_ok=True)
        elif path.is_file():
            new_path.touch()


if __name__ == '__main__':
    # arguments by hand
    source_str = './temp'
    target_str = './temp2/'

    argv = sys.argv
    if len(argv) == 3:
        source_str, target_str = argv[1] = argv[2]

    source = Path(source_str)
    target = Path(target_str)
    dummy_maker(source, target)
