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
        