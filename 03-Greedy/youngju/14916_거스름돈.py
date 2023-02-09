n = int(input())
units = n % 10
answer = 0

if units == 0 or units == 5:
    answer = n // 5
elif units == 1 or units == 6:
    # n이 1일때
    if n < 5:
        answer = -1
    else:
        # answer = (n // 5 - 1) + 3
        answer = n // 5 + 2
elif units == 2 or units == 7:
    answer = n // 5 + 1
elif units == 3 or units == 8:
    # n이 3일때
    if n < 5:
        answer = -1
    else:
        # answer = (n // 5 - 1) + 4
        answer = n // 5 + 3
elif units == 4 or units == 9:
    answer = n // 5 + 2

print(answer)
