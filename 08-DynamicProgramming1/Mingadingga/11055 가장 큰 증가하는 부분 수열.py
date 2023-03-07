import sys

read = sys.stdin.readline
n = int(read())
numbers = list(map(int, read().split()))
dp = numbers[:]

'''
dp[i] : i번째 요소를 포함했을 때 증가하는 수열의 최대 합

1) numbers[i] >= numbers[i 전의 것] : 증가함. dp[i] = max(dp[i], dp[i 전의 것] + numbers[i])
2) numbers[i] < numbers[i-1] : 감소함. 누적합에 반영 안함

'''

for i in range(n):
    for j in range(0, i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j] + numbers[i])

print(max(dp))