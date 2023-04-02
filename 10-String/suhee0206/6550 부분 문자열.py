import sys

read = sys.stdin.readline
while line := read():
  s, t = line.split()
  i = 0
  for x in t:
    if x == s[i]:
      i += 1
    if i == len(s):
      print("Yes")
      break
  else:
    print("No")