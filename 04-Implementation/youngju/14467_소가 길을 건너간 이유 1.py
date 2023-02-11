import sys

n = int(sys.stdin.readline().strip())
cow = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dic = {}
answer = 0
for i in range(n):
    if cow[i][0] not in dic.keys():
        dic[cow[i][0]] = cow[i][1]
    else:
        if cow[i][1] != dic[cow[i][0]]:
            dic[cow[i][0]] = cow[i][1]
            answer += 1
        else:
            dic[cow[i][0]] = cow[i][1]

print(answer)




