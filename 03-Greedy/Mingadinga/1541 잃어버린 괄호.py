def calculate_term(term):
  plus_numbers = term.split('+')
  result = 0
  for number in plus_numbers:
    result += int(number)
  return result

expression = input()
plus_term = expression.split('-')

result = calculate_term(plus_term[0])
for i in range(1, len(plus_term)):
  # eval은 0으로 시작하는 숫자는 못 읽더라
  # result -= eval(plus_term[i])
  result -= calculate_term(plus_term[i])

print(result)