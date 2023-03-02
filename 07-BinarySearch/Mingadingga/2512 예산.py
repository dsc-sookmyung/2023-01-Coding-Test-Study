import sys

read = sys.stdin.readline
n = int(read())
requests = list(map(int, read().split()))
total = int(read())

'''
1. 상한선이 mid 값일 때 지급 가능한 예산 총액을 구한다
2. 계산한 총액이 보유 총액보다 작다면, 상한선을 더 올려도 된다는 뜻이므로 오른쪽을 탐색한다. 상한선의 최댓값을 찾고 있으므로 이때 결과값을 업데이트한다.
3. 계산한 총액이 보유 총액보다 크다면, 상한선을 내려야 한다는 뜻이므로 왼쪽을 탐색한다.
'''


def search_max_limit(start, end, requests, total):
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        able_total = calculate_able_total(requests, mid)
        if able_total <= total:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1
    return answer


def calculate_able_total(requests, mid):
    result = 0
    for request in requests:
        if request < mid:
            result += request
        else:
            result += mid
    return result


if sum(requests) < total:
    print(max(requests))
else:
    print(search_max_limit(1, max(requests), requests, total))