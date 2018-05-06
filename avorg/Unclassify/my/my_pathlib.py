from pathlib import Path
import rstr

# for i in range(10):
#     print(rstr.xeger(r'[A-Z]{3}-\d{3}\.mp4'))

# p = Path('./Done/test.txt')
# p = Path('./Done/')
# p.write_text('text')

file_list = [x for x in Path('./Yet/').iterdir() if x.is_file()]
print(file_list)
for i in file_list:
    print(i.stem)
    i.rename(Path('./Done/') / i.name)
