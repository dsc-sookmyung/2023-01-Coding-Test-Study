bar = list(input())
answer = 0
res = []

for i in range(len(bar)):
    if bar[i] == '(':
        res.append('(')

    else:
        if bar[i-1] == '(': 
            res.pop()
            answer += len(st)

        else:
            res.pop() 
            answer += 1 

print(answer)