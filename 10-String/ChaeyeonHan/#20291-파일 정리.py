import sys
input = sys.stdin.readline

N = int(input())
files = [input().rstrip() for _ in range(N)]

result = {}
for i in range(N):
    a, b = files[i].split(".")  # sbrus txt
    if b in result:
        result[b] += 1  # 해당 확장자 파일 1 증가
    else:
        result[b] = 1

result = list(result.items())  # 딕셔너리 -> 리스트 변환
result.sort(key=lambda x: x[0])

for i in range(len(result)):
    print(result[i][0], result[i][1])