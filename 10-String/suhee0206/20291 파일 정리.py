import sys

read = sys.stdin.readline
N = int(read())
extension_dict = dict()
for _ in range(N):
  extension = read().rstrip().split('.')[1]
  if extension in extension_dict:
    extension_dict[extension] += 1
  else:
    extension_dict[extension] = 1
sorted_extension_dict = sorted(extension_dict.items())
for item in sorted_extension_dict:
  print(item[0], item[1])