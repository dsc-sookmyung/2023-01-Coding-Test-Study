import sys

read = sys.stdin.readline
s = int(read())

def binary_search(start, end):
    answer = s
    while start <= end:
        mid = (start + end) // 2
        total = (mid * (mid + 1)) // 2
        # 최댓값 찾으니까 이왕이면 오른쪽으로 범위를 좁힐 때 저장
        if total <= s:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    return answer

print(binary_search(1, s))