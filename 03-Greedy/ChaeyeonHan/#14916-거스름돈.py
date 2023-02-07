import sys
input = sys.stdin.readline

n = int(input())
count = 0  # 동전의 갯수

while True:
    if n % 5 == 0:  # 5의 배수라면
        count += n // 5
        break
    else:
        n -= 2
        count += 1
    if n < 0:
        break
if n < 0:
    print(-1)
else:
    print(count)