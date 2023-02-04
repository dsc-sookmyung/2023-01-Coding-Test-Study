## 1620 나는야 포켓몬 마스터 이다솜

### 풀이
도감 번호가 주어졌을 때와 포켓몬 이름이 주어졌을 때 두가지 경우를 검색해야 하기 때문에
그냥 두가지의 Dict를 만들어 정보를 입력받을 때 두번 저장하도록 했다.
이후 검색할 때에 isdigit() 함수를 이용해 번호인지 이름인지 파악한 후 알맞게 찾을 수 있도록 풀어나갔다

**Dict를 선택한 이유**
배열로 할 수있었지만, 배열의 검색같은 경우에는 모든 index를 돌아야 하기 때문에 시간 복잡도가 O(n)이 나와 시간 초과가 나오게 된다. 따라서 시간복잡도가 O(1)인 Dict와 set 중 Dict를 이용했다

```
import sys

n, m = map(int, input().split())


int_key = {}  #Dict로 검색시 시간복잡도를 낮춤
name_key = {}  
for i in range(n):
    name = sys.stdin.readline().strip()
    int_key[i] = name
    name_key[name] = i


for _ in range(m):
    item = sys.stdin.readline().strip()
    if item.isdigit() == True:
        print(int_key[int(item)-1])
    else:
        print(name_key[item]+1)
```

## 2075 N번째 큰 수

### 풀이
N*N의 배열에서 N 번째 큰 수를 구해야 한다. heap을 이용해 뒤에서부터 제거하여 구할까 하다가 N개의 힙을 유지하면서 큰 값이 들어올 때만 작은값을 pop 한 후 큰 값을 push 하여 전체 for문을 반복한다. 반복문의 결과로서는 heap에 5개의 item이 있는데, N번째 큰 수, N-1번째 큰 수 ... 1번째 큰수 순서대로 정렬되있다.

**추가**
heapq는 기본적으로 minheap이다

```
import heapq

N = int(input())

heap= []
for _ in range(N):
    tmp = map(int,input().split())
    for i in tmp:
        if(len(heap)<N):
            heapq.heappush(heap,i)
        else:
            if heap[0] <i:
                heapq.heappop(heap)
                heapq.heappush(heap,i)
                
            
print(heap[0])
```


## 11279 최대 힙

### 풀이
앞의 2075에서 사용한 heap을 이용하는 문제이다. 대신 minheap대신 maxheap을 사용해 구현한다.
maxheap과 같이 사용하기 위해선 `heapq.heappush(MaxHeap,-x)` 이렇게 들어갈 값에 마이너스를 취해준다 (부호를 반대로 저장)
부호를 반대로 저장하였기 때문에 pop 할 때에는 `-heapq.heappop(MaxHeap))` 맨 앞에 마이너스를 붙여 다시 양수(혹은 음수)로 복원시켜 빠져나오도록 한다

**추가**
`int(input())` 를 사용했더니 시간초과가 생겼다.. 더 빠른 `int(sys.stdin.readline())`을 사용하자

```
#11279 최대 힙

import heapq
import sys
N =  int(input())
MaxHeap = []
for _ in range(N):
    x= int(sys.stdin.readline())# input 사용 시 시간초과
    if x ==0:
        if(not MaxHeap):
            print(0)
        else:
            print(-heapq.heappop(MaxHeap))
    else:
        heapq.heappush(MaxHeap,-x) #heapq는 기본적으로 minHeap
```

## 문자열 집합

### 풀이
주어진 문자열들이 S집합에 몇개 해당되는지 갯수를 세어야한다. 
처음에는 배열로 전체탐색을 통해 파악했는데 시간초과로 인해 검색 속도 O(1)인 set,dict 중 set를 이용했다

```
# 문자열 집합

import sys

N,M = map(int,input().split())
S = set() # 배열로 검색시 시간 초과 
count =0
for _ in range(N):
    tmp = sys.stdin.readline()
    S.add(tmp)
    # print("집합 S에 포함되어있는 문자열")
for _ in range(M):
    test = sys.stdin.readline()
    if( test in S): # 배열은 시간복잡도 O(n), 집합,Dict는 O(1)
        count = count + 1
    # print("검사해야하는 문자열")
print(count)
```