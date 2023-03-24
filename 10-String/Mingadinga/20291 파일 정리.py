import sys
read = sys.stdin.readline

n = int(read())
files = [read().rstrip() for _ in range(n)]
d = {}

for file in files:
  file_name, file_extension = file.split('.')
  if file_extension not in d.keys():
    d[file_extension] = 1
  else:
    d[file_extension] += 1

result = sorted(d.items(), key=lambda d:d[0])
for extension, count in result:
  print(extension, count)