S = int(input())
answer = 0
result = 0
for i in range(1, S+1):
    result += i
    if result == S:
        answer = i
    if result > S:
        answer = i - 1
        break
print(answer)

