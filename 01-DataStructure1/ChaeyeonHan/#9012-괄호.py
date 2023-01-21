'''
[시도]
    입력받은 괄호 문자열을 스택에 넣고 괄호를 하나씩 꺼내며 괄호 방향을 확인한다.
    방향이 언제 달라지는지 주목한다. 방향이 달라진다면, 이전 괄호 방향의 갯수를 감소시킨다.
    맨 마지막까지 확인하고, x y의 갯수가 0으로 일치한다면 => 올바른 괄호
    갯수뿐만 아니라 짝이 맞는지(?)도 확인해줘야 하는데?
    ()))(( 이런건 올바르지 않은 예시인데 어떻게 올바르지 않다고 하지?......

[해설]
    입력이 들어오면 스택에 다 넣고 한개씩 빼는 방법 말고.. 한개씩 값을 확인하며 경우를 나눠 스택에 넣어준다.
    '(' 괄호가 들어오면 append로 스택에 추가
    ')' 괄호가 들어오면, 스택에 있던 '('를 pop해서 꺼내준다. 꺼낼 '(' 괄호가 없다면, 짝이 맞지 않기에 올바르지 않은 괄호

'''

# 풀이 1
T = int(input())
for _ in range(T):
    PS = input()
    stack = []  # 빈 스택
    for i in PS:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                stack.append(i)
                break
            else:
                stack.pop()
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')

# 풀이 2(비슷한 방법)
T = int(input())
for _ in range(T):
    PS = list(input())
    cnt = 0
    for i in PS:
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt -= 1
        if cnt < 0:  # ')' 없이 '('가 온 경우
            print('NO')
            break
    if cnt == 0:
        print('YES')
    elif cnt > 0:
        print('NO')
