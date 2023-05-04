import sys
read = sys.stdin.readline

def is_s_done(s_index, s):
  if s_index == len(s):
    return True

while True:
  ss = read().rstrip()
  if not ss:
    break
  s, t = ss.split()
  t_index, s_index = 0, 0
  is_sub_string = False

  while s_index < len(s) and t_index < len(t):
    if t[t_index] == s[s_index]:
      s_index += 1
      is_sub_string = is_s_done(s_index, s)
      if is_sub_string: break
    t_index += 1

  if is_sub_string: print("Yes")
  else: print("No")
