# BOJ 9012 괄호 
## 풀이과정
> Stack 자료구조 관련 문제
1. 테스트 데이터의 개수 T와 괄호 문자열을 담을 string, 스택 필요
2. 만약 "("를 입력받는다면 스택에 Push
3. ")"를 입력받았고 스택이 empty 상태가 아니라면 pop   
    3-1. 스택이 empty 상태라면 VPS가 아니므로 "NO" 출력
4. 문자열의 마지막      
   4-1. 스택이 비어있다면 VPS이므로 "YES" 출력   
   4-2. 그렇지 않으면 "NO" 출력

## 시간 복잡도
O(N)

## Stack
> 한 쪽 끝에서만 자료를 넣고 뺄 수 있는 LIFO(Last In First Out) 형식의 자료 구조
- Stack 헤더 파일   
  ```#include <stack>```
- Stack 선언    
  ```stack<data type> name;```
- pop(): 스택에서 가장 위에 있는 항목을 제거
- push(item): item을 스택의 가장 윗부분에 추가
- top(): 스택 최상위 데이터 반환
- size(): 스택의 현재 사이즈 반환
- empty(): 스택이 비어있는지 확인
- swap(stack1, stack2): 두 스택의 내용을 교환

# BOJ 1158 요세푸스 문제
## 풀이과정
> Queue 자료구조 관련 문제
1. 입력은 사람수인 N과 제거할 번째인 K
2. 큐를 사용하므로 큐 선언
3. 사람 수만큼 큐에 push
4. 큐 사이즈가 1이 될 때까지 반복   
   4-1. k-1 만큼 큐에서 빼내고 뒤로 다시 넣음   
   4-2. q.front를 출력하고 pop
5. 큐 사이즈가 1이면 마지막 숫자이므로 출력
   
## 시간 복잡도
O(N)

## Queue
> 처음 넣은 데이터가 처음으로 빠져나오는 FIFO(First In First Out) 형식의 자료구조
- Queue 헤더 파일   
  ```#include <queue>```
- Queue 선언   
  ```queue<data type> name;```
- pop(): 큐의 front data 삭제
- push(item): 큐에 item 추가
- front(): 최상위 데이터 반환
- back(): 가장 마지막 데이터 반환
- size(): 큐의 현재 사이즈 반환
- empty(): 큐가 비어있는지 확인
- swap(queue1, queue2): 두 큐의 내용을 교환
  
# BOJ 1966 프린터 큐
## 풀이과정
> Queue, 우선순위큐
1. 입력값을 담을 n, m과 결과값 res, queue와 priority_queue 선언
2. n만큼 중요도 값을 받아와서 queue에는 순서와 함께 push, priority_queue에는 중요도를 push
3. q가 비어있지 않다면
   3-1. queue의 가장 앞에 있는 index와 중요도 값을 저장 후 pop
   3-2. priority_queue의 가장 앞 중요도와 queue에서 저장한 중요도 값이 같으면 priority_queue를 pop하고 res++
        3-2-1. 그 인덱스 값이 m이라면 현재 res값 출력
    3-3. 중요도 값이 다르다면 큐 가장 뒤에 다시 push


## 시간 복잡도
O(${N^{2logn}}$)

## 우선순위 큐
> Queue의 한 종류로 우선순위에 따라 정렬된 Queue
- 헤더 파일   
  ```#include <queue>```
- 선언
  ```
  // 변수들을 비교함수에 따라 정렬
  priority_queue<자료형, Container, 비교함수> 변수명;
  // 내림차순에 따라 정렬  
  priority_queue<자료형> 변수명;
  ```
- pop(): 맨 앞에 있는 원소 삭제
- push(item): item 삽입
- top(): 맨 앞에 있는 원소 반환
- empty(): 큐가 비어있는지 확인
- size(): 큐의 크기 반환

# BOJ 10799 쇠막대기
## 풀이과정
> Stack 자료구조 관련 문제
1. 접근   
   1-1. '('가 나온 뒤 바로 ')'가 나오면 레이저
   1-2. ')'가 나온 뒤 ')'가 나오면 막대기가 끝나는 지점
   1-3. 레이저가 나오면 존재하는 막대기들은 모두 한 번씩 잘림
2. 괄호 문자열을 담을 string과 stack, 결과를 담을 res 변수 선언
3. 문자열 길이만큼 for문   
   3-1. '('라면 push
   3-2. ')'라면
        3-2-1. 이전 값이 ')'일 경우 막대가 끝나므로 스택에서 pop하고 res++
        3-2-2. 이전 값이 '('일 경우 레이저이므로 pop하고 현재 있는 막대의 수만큼 res에 더해줌
4. 결과 값 출력
   
## 시간 복잡도
O(N)

## Stack
> 한 쪽 끝에서만 자료를 넣고 뺄 수 있는 LIFO(Last In First Out) 형식의 자료 구조
- Stack 헤더 파일   
  ```#include <stack>```
- Stack 선언   
  ```stack<data type> name;```
- pop(): 스택에서 가장 위에 있는 항목을 제거
- push(item): item을 스택의 가장 윗부분에 추가
- top(): 스택 최상위 데이터 반환
- size(): 스택의 현재 사이즈 반환
- empty(): 스택이 비어있는지 확인
- swap(stack1, stack2): 두 스택의 내용을 교환