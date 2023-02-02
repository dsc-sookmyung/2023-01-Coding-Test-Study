import sys
import heapq

input = sys.stdin.readline
heap = []
N = int(input())

for _ in range(N):
    num = int(input())
    if num != 0:
        heapq.heappush(heap, -num)  # 0이 아니면 최대힙에 넣어주기
    else:
        if len(heap) != 0:  # 힙이 비어있지 않다면 max 출력
            print(-heapq.heappop(heap))
        else:
            print(0)