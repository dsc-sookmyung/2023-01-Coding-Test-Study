import sys
input = sys.stdin.readline

def is_pseudo(words, left, right):  # 유사회문인지
    while left < right:
        if words[left] == words[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

def is_palindrome(words, left, right):  # 회문인지
    while left < right:
        if words[left] == words[right]:
            left += 1
            right -= 1
        else:
            check_left = is_pseudo(words, left + 1, right)
            check_right = is_pseudo(words, left, right - 1)
            if check_right or check_left:
                return 1
            else:
                return 2
    return 0



N = int(input())
for _ in range(N):
    words = input().rstrip()
    left , right = 0, len(words)-1
    ans = is_palindrome(words, left, right)
    print(ans)