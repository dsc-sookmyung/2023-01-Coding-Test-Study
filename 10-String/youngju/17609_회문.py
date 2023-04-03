import sys

read = sys.stdin.readline

def check(str, left, right):
    while left < right:
        if str[left] == str[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

T = int(input())
strings = [list(read().strip()) for _ in range(T)]

for string in strings:
    if string == string[::-1]:
        print(0)
    else:
        left = 0
        right = len(string) - 1
        while left < right:
            if string[left] == string[right]:
                left += 1
                right -= 1
            else:
                if check(string, left+1, right) or check(string, left, right-1):
                    print(1)
                    break
                else:
                    print(2)
                    break



