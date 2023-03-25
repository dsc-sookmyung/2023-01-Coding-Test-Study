import sys
input = sys.stdin.readline

words_list = [input().rstrip() for _ in range(5)]
result = []
for i in range(15):
    for j in range(5):
        if len(words_list[j]) > i:
            result.append(words_list[j][i])

print(''.join(result))
# 인덱스 순서는
# [0][0], [1][0], [2][0], [3][0], [4][0], [0][1],