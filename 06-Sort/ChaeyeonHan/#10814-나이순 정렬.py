import sys
n = int(sys.stdin.readline())

members=[]
for _ in range(n):
    a, b = sys.stdin.readline().split()
    a = int(a)  # 숫자로 바꿔주기
    members.append([a, b])

sorted_members = sorted(members, key=lambda x: x[0])
# 나이순으로 먼저 정렬, 나이 같다면 가입한 순으로(정렬하면 가입순으로 나온다!)

for i in range(n):
    print(sorted_members[i][0], sorted_members[i][1])
