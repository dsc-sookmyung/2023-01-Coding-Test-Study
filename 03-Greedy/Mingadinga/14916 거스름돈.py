import sys

balance = int(input())
coin_count = 0

while True:
    if balance % 5 == 0: # 5원짜리 사용 가능
        coin_count += balance // 5
        break
    else: # 2원짜리 사용할 수 있도록 차감
        balance -= 2
        coin_count += 1

    if balance < 0: # 더이상 거슬러줄 수 없음
        break

if balance < 0:
    print(-1)
else:
    print(coin_count)