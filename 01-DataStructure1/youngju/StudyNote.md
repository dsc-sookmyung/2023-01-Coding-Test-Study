﻿## 1966 프린터 큐
m이 빠져나온 것을 -1이라고 생각하고 -1이 될 때까지 다음 과정 진행 : 

i) 중요도 순으로 제거하기 위해서 중요도가 가장 큰 것이 맨 앞에 있으면 삭제 
-> result(m이 몇 번째에 빠져나가는지 카운트) 증가
ii) 중요도가 가장 큰 것이 맨 앞에 있지 않으면 맨 뒤로 보내고 삭제 
-> 맨 뒤로 보낼때 m이 어디에 있었는지 기억하기 위해 m위치도 조정

## 10799 쇠막대기
스택 이용

"(" 일 경우 스택에 일단 append
")"일 경우 레이저인지 아닌지 구분해야함
-> ")"일 때 바로 이전 문자가 "("라면 레이저이므로 스택 길이만큼 쇠막대기 개수 더하기
-> 바로 이전 문자가 "(" 가 아니라 ")"라면 쇠막대기이므로 +1

## 1158 요세푸스 문제
deque 이용

사람 수 만큼 deque(circle)에 1부터 n까지 저장
-> circle에서 k번째 사람을 삭제하기 위해 k-1까지는 popleft한 다음 다시 append
-> 마지막 k번째는 popleft하고 정답 리스트에 추가

## 9012 괄호
스택 이용

문자열을 받은 후 "("라면 일단 스택에 append
-> ")"라면 스택에서 pop하는데 스택이 비었다면 바로 NO출력
-> 모든 문자열을 돌았을 때 스택이 비었다면 YES출력하고 그렇지 않으면 NO출력