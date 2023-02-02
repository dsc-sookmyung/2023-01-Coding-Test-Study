# 최대힙을 구현해 N번째로 큰 수 출력하기 => 메모리 초과
# import sys, heapq
#
# input = sys.stdin.readline
# N = int(input())
#
# heap = []
# for _ in range(N):
#     arr = list(map(int, input().split()))
#     for i in arr:
#         heapq.heappush(heap, -i)  # 최대힙 구현
# for i in range(N-1):
#     heapq.heappop(heap)
# print(-heapq.heappop(heap))


# 다른 풀이 : 최소힙의 크기를 n만큼 유지하기
import sys, heapq

input = sys.stdin.readline
heap = []
N = int(input())

for i in range(N):
    arr = list(map(int, input().split()))
    if not heap:  # 힙이 비어있으면(첫번째 입력시)
        for value in arr:
            heapq.heappush(heap, value)
    else:
        for value in arr:
            if heap[0] < value:  # 힙에 들어있는 값보다 크다면 힙에 있는 값 빼고 value 넣어주기
                heapq.heappop(heap)
                heapq.heappush(heap, value)
print(heap[0])
# print(heapq.heappop(heap))