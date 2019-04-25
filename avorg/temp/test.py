import re

# x = re.search(r'^[a-zA-Z]{2,5}-?[a-z]{2,5}\.(?:mp4|avi)', 'ebod-001.avi')
x = re.search(r'[0-9]{2,5}\.(mp4|avi)', 'ebod-001.avi')
print(x)