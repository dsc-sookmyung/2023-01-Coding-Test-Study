# 10798 세로 읽기
import sys


arr = []
lines = []
ans = ''
for _ in range(5):
    tmp = sys.stdin.readline().rstrip()
    tmp_line = len(tmp)
    lines.append(tmp_line)
    arr.append(tmp)

line_max = max(lines)

for i in range(line_max):
    for j in range(5):
        if i < lines[j]:
            ans = ans + arr[j][i]
print(ans)