t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    star = list(map(int, input().split()))
    result = 0
    while m != -1:
        if star[0] == max(star):
            del star[0]
            m -= 1
            result += 1
        else:
            star.append(star[0])
            del star[0]
            if m == 0:
                m = len(star) - 1
            else:
                m -= 1

    print(result)