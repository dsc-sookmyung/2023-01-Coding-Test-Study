import sys

read = sys.stdin.readline
n, m = map(int, read().split())
pokedex  = [read().rstrip() for _ in range(n)]
questions = [read().rstrip() for _ in range(m)]

for question in questions:
  if question.isdigit():
    print(pokedex[int(question) - 1])
  else:
    print(pokedex.index(question) + 1)
