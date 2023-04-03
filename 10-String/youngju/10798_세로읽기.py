import sys

read = sys.stdin.readline

words = [read().strip() for _ in range(5)]
cnt = 0
for i in range(5):
    cnt = max(len(words[i]), cnt)

answer = ""
tmp = 0
while cnt > 0:
    for i in range(5):
        if tmp + 1 > len(words[i]):
            continue
        else:
            answer += words[i][tmp]
    tmp += 1
    cnt -= 1

print(answer)
