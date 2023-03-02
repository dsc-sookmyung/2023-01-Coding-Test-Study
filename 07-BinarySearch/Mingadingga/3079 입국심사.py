import sys

read = sys.stdin.readline
n, m = map(int, read().split())
counters = [int(read()) for _ in range(n)]
start, end = 0, max(counters) * m
answer = 0

'''
심사에 걸리는 시간을 상한값으로 두고 탐색한다.
상한값이 조정되는 조건은 제한 시간 안에 심사를 받을 수 있는 사람의 수로 한다.
- 심사 가능 인원 < 총 인원: 부족함. 상한값 올려서 오른쪽 탐색
- 심사 가능 인원 >= 총 인원: 여유 있음. 상한값 줄여서 왼쪽 탐색, 최솟값 구하니까 줄일 때 결과 업데이트
'''

def calculate_able_count(delays, time_limit):
  able_count = 0
  for delay in delays:
    able_count += (time_limit // delay)
  return able_count

while start <= end:
  mid = (start + end) // 2
  able_count = calculate_able_count(counters, mid)
  if able_count < m:
    start = mid + 1
  else:
    end = mid - 1
    answer = mid

print(answer)