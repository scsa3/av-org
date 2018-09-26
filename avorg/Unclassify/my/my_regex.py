import re

# _pattern = r'((?!HD(?:1080|720))[[:alpha:]]{2,4}-?\d{3,4}|)'
pattern = r'[a-z]{2,4}-?\d{3,4}'
string = 'dmm1002'

# prog = re.compile(_pattern)
# result = prog.match(string)

result = re.match(pattern, string)

print(result.string)
print(result)

string = '2016/09/13 (DVD セル版)'

