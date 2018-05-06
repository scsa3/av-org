from pathlib import Path


def my_rename():
    file_path = Path('abc999.mp4')
    target_directory = Path('./abc')
    target_directory.mkdir(parents=True, exist_ok=True)
    file_path.rename(target_directory.joinpath(file_path))


def my_list_files():
    p = Path('./')
    files = list(p.glob('*.mp4'))
    print(files)
    return files


def my_mkdir():
    p = Path('./')
    p.mkdir('test')


def check_directory():
    unclassified_path.mkdir(parents=True, exist_ok=True)
    classified_path.mkdir(parents=True, exist_ok=True)


if __name__ == '__main__':
    # check directory
    unclassified_path = Path('./unclassified')
    classified_path = Path('./classified')
    unclassified_path.mkdir(parents=True, exist_ok=True)
    classified_path.mkdir(parents=True, exist_ok=True)
    # list file in unclassified
    files = list(unclassified_path.glob('*'))
    # rename file and move them
    for file in files:
        new_path = classified_path.joinpath(file.name)
        file.rename(new_path)
