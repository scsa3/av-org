from pathlib import Path

list_file = [x for x in Path('./Done').iterdir() if x.is_file()]
for f in list_file:
    f.rename(Path('./Yet') / f.name)
