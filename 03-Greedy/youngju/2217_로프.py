import sys

n = int(sys.stdin.readline())
rope = [int(sys.stdin.readline()) for _ in range(n)]
rope.sort(reverse=True)

answer = 0
for i in range(n):
    if rope[i] * (i + 1) > answer:
        answer = rope[i] * (i + 1)

print(answer)


