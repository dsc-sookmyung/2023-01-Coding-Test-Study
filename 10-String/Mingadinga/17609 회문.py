import sys

read = sys.stdin.readline


def check_palindrome(word):
    if word[:] == word[::-1]: return 0

    l_index, r_index = 0, len(word) - 1
    while l_index < r_index:
        if word[l_index] == word[r_index]:
            l_index += 1
            r_index -= 1
        else:
            # 유효한 범위이면
            if l_index < r_index:
                # 왼쪽 제거
                temp = word[:l_index] + word[l_index + 1:]
                if temp[:] == temp[::-1]: return 1
                # 오른쪽 제거
                temp = word[:r_index] + word[r_index + 1:]
                if temp[:] == temp[::-1]: return 1
            return 2


n = int(read())
words = [read().rstrip() for _ in range(n)]

for word in words:
    print(check_palindrome(word))