import sys

read = sys.stdin.readline
T = int(read())

def isPalindrome(string):
  for i in range(len(string)//2):
    last_index = len(string) - 1
    if string[i] != string[last_index - i]:
      return False
  return True

def answer(string):
  if isPalindrome(string):
    return 0
  for i in range(len(string)//2):
    last_index = len(string) - 1
    if string[i] != string[last_index - i]:
      string_one = string[:i] + string[i+1:last_index+1]
      if isPalindrome(string_one):
        return 1
      string_two = string[:last_index-i] + string[last_index-i+1:]
      if isPalindrome(string_two):
        return 1
      else:
        return 2

for _ in range(T):
  string = list(read().rstrip())
  print(answer(string))