import sys

read = sys.stdin.readline
N = int(read())

scores = []

for _ in range(N):
  score = read().split()
  # 성적은 string에서 int로 타입 변경
  for i in range(len(score)):
    if score[i].isdigit():
      score[i] = int(score[i])
  scores.append(score)

sorted_scores = sorted(scores, key = lambda x : (-x[1], x[2], -x[3], x[0])

for x in sorted_scores:
  print(x[0])