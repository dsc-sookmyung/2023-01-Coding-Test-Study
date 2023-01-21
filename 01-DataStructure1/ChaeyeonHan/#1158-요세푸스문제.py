'''
[시도]
    사람 수만큼 1~N까지의 숫자가 들어있는 배열을 돌면서
    i 가 k의 배수가 된다면 그 사람 제거 -> result.append()
    배열을 돌면서 i가 len(배열)과 같아진다면 맨 앞으로 이동하여 다시 반복

[해설]
    사람을 원에서 빼면, 뒤에 있는 나머지 사람들의 인덱스가 변한다는 것을 생각 못했다.
    그래서 K가 아니라 K-1씩 증가시켜야 한다
'''

# 풀이1
N, K = map(int, input().split())
result = []  # 제거된 사람 목록
circle = [i for i in range(1, N+1)]

num = 0
for i in range(N):
    num += K-1
    if num >= len(circle):
        num %= len(circle)
    result.append(str(circle.pop(num)))

# print("<", ", ".join(result), ">", sep="")  # sep을 추가해서 <, >, 숫자들 사이에 공백이 없도록
print("<" + ", ".join(result) + ">")

# 풀이2
N, K = map(int, input().split())
circle = [i for i in range(1, N+1)]

result = []
del_idx = K-1

while circle:
    result.append(str(circle.pop(del_idx)))
    if len(circle) == 0:
        break
    del_idx = (del_idx + K-1) % len(circle)

print("<" + ", ".join(result) + ">")