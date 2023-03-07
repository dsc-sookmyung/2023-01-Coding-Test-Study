import sys

read = sys.stdin.readline
k, n = map(int, read().split())
lengths = [int(read()) for _ in range(k)]

'''
1. 탐색 범위는 가장 긴 막대에서 시작해 줄여나간다.
2. 길이가 mid 값일 때 만들 수 있는 랜선의 최대 개수를 구한다.
3. 개수가 n보다 작다면, 길이를 줄여야 하므로 왼쪽을 탐색한다.
4. 개수가 n보다 크다면, 길이를 늘여야 하므로 오른쪽을 탐색한다. 
잘리는 개수가 n보다 커도 되기 때문에 개수 == n인 경우도 큰 경우와 동일하게 취급한다.
이 문제는 잘리는 최대 길이를 구하는 것이므로 탐색이 끝났을 때 end를 출력해야한다.
'''


def search_max_cnt(start, end, lengths, n):
    while start <= end:
        mid = (start + end) // 2
        able_cnt = calculate_able_cnt(lengths, mid)
        if able_cnt < n:
            end = mid - 1
        else:
            start = mid + 1
    return end


def calculate_able_cnt(lengths, mid):
    result = 0
    for length in lengths:
        result += (length // mid)
    return result


print(search_max_cnt(1, max(lengths), lengths, n))