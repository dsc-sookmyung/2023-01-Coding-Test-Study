task_count = int(input())
pattern = input()

# 연속된 경우 제외하고 첫 문자 개수만 세어야함
paint_count = {'B': 0,'R': 0}

paint_count[pattern[0]] += 1

for i in range(1, task_count):
  if pattern[i] != pattern[i-1]:
    paint_count[pattern[i]] += 1

print(min(paint_count.values()) + 1)