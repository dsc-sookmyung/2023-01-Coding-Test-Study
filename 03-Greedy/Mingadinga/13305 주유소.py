import sys

read = sys.stdin.readline

city_count = int(input())
city_length = list(map(int, read().split()))
oil_price = list(map(int, read().split()))

# 런타임 에러 났던 코드
# 파이썬으로 한줄 입력을 받으면 문자열을 공백으로 나눠서 리스트로 변환해야하므로
# stdin으로 입력받아 split()으로 나누고 정수형 리스트로 변환하는 코드로 고쳤다
# 단순 input()은 한줄 입력을 int로 바꾸지 못하므로 오류 발생한 것.
# https://www.acmicpc.net/board/view/10856 참고
# for i in range(city_count - 1):
#     city_length.append(int(input()))
#
# for i in range(city_count):
#     oil_price.append(int(input()))

min_oil_price = oil_price[0]
min_total_price = min_oil_price * city_length[0]
for i in range(1, city_count - 1):
    if min_oil_price > oil_price[i]:
        min_oil_price = oil_price[i]
    min_total_price += min_oil_price * city_length[i]

print(min_total_price)