from Unclassify.file_format import video
from pathlib import Path, WindowsPath

handle_path = WindowsPath(r'X:\GoogleDrive\Local\Videos\Porn\Unclassify')
target_path = WindowsPath(r'X:\GoogleDrive\Local\Videos\Porn\!!')
delete_path = WindowsPath(r'X:\GoogleDrive\Local\Videos\Porn\!delete')


def file_search(path=Path(r'.'), pattern=r'**/*'):
    file_paths = path.glob(pattern)
    for file_path in file_paths:
        print(file_path)


def video_search(path=Path(r'.')):
    file_paths = list()
    for extension in video:
        file_paths.extend(path.glob(r'**/[a-z][a-z][a-z][a-z][a-z]-[0-9][0-9][0-9].{}'.format(extension)))
    for file_path in file_paths:
        print(file_path)
    return file_paths


def get_pair_image(video_paths=list()):
    image_paths = list()
    for video_path in video_paths:
        image_path = video_path.parent / str(video_path.stem + '.jpg')
        if image_path.exists():
            print(image_path)
            image_paths.append(image_path)
    return image_paths


def get_directory_size(path=Path('.')):
    total_size = 0
    for content in path.glob(r'**\*'):
        total_size += content.stat().st_size
    # print(total_size)
    # print('{} GB'.format(total_size / 1024 / 1024 / 1024))
    return total_size


def replace_file(paths=list()):
    for i in paths:
        # print(i)
        i.replace(target_path.joinpath(i.name))


def replace_dir(path=Path()):
    path.replace(delete_path.joinpath(path.name))


def delete_small_dirs(path=handle_path, threshold_size=10 * 1024 * 1024):
    x = path.glob('*')
    for i in x:
        if i.is_dir():
            # print(i.name)
            if get_directory_size(i) < threshold_size:
                print(i.name)
                print(get_directory_size(i))
                replace_dir(i)


if __name__ == '__main__':
    # file_search(handle_path, r'**/*.avi')
    # get_directory_size(Path(r'X:\GoogleDrive\Local\KodiTest'))
    video_paths = video_search(handle_path)
    image_paths = get_pair_image(video_paths)
    replace_file(video_paths)
    replace_file(image_paths)
