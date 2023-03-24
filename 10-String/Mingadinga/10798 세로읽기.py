import sys
read = sys.stdin.readline

words = [read().rstrip() for _ in range(5)]
words_length = [len(word) for word in words]
result = []

for i in range(max(words_length)):
  for j in range(5):
    if words_length[j] <= i:
      continue
    result.append(words[j][i])

print(''.join(result))