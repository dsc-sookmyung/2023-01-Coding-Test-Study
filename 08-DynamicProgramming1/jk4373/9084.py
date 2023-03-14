import sys 

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    M = list(map(int,sys.stdin.readline().split()))
    money = int(sys.stdin.readline())

    dp = [0] * (money+1) # 0원 만드는 방법은 항상 1
    dp[0] =1
    for mm in M:
        for i in range(1,money+1):
            if i >= mm:
                dp[i] += dp[i -mm]
    print(dp[money])