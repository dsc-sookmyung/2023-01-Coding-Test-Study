'''
[해설]
    deque의 rotate()함수를 사용해서 리스트 회전이 가능하다!
    음수 : 왼쪽 회전, 양수 : 오른쪽 회전

    문제에서 초기 상태의 인덱스에 담겨 있는 문서가 몇번째로 pop되는지를 물어봤기에, rotate시 초기 상태의 인덱스 정보를 함께 가져가야한다.
    => idx = deque(range(0, N))를 만들어서 인덱스를 저장해서 문서가 이동할때 함께 이동

    ex)
    test = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    test.rotate(2) 를 적용해주면,
    test = [8, 9, 1, 2, 3, 4, 5, 6, 7]
'''

import sys
from collections import deque
T = int(input())

for _ in range(T):
    N, target = map(int, sys.stdin.readline().rstrip().split())
    priority = deque(list(map(int, sys.stdin.readline().rstrip().split())))  # 중요도 입력받기
    idx = deque(range(0, N))
    cnt = 0  # 몇번째 인쇄인지

    while priority:
        if priority[0] == max(priority):
            cnt += 1
            priority.popleft()
            if idx.popleft() == target:  # 지금 popleft한 문서가 target이면
                print(cnt)
                break
        else:  # 가장 높은 중요도가 아니라면 deque의 맨 뒤로 이동시킨다
            priority.rotate(-1)
            idx.rotate(-1)



