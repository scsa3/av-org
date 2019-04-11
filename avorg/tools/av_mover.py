import sys
from pathlib import Path
from tools.video_finder import videos_finder


def av_mover(source_directory: Path, target_directory: Path) -> None:
    videos = videos_finder(source_directory)
    for path in videos:
        new_path = target_directory / path.name
        path.rename(new_path)


if __name__ == '__main__':
    # arguments by hand
    source_str = '../temp/source'
    target_str = '../temp/target'

    argv = sys.argv
    if len(argv) == 3:
        source_str, target_str = argv[1] = argv[2]

    source = Path(source_str)
    target = Path(target_str)
    av_mover(source, target)
