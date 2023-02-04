#2217 로프
import sys
n = int(input())
w = []
for _ in range(n):
    tmp = int(sys.stdin.readline())
    w.append(tmp)
w.sort(reverse=True)
for i in range(len(w)):
    w[i] = w[i]*(i+1)
# print(min(w)*n ) # 왜 아니지?? 생각해보니 압도적으로 높은 하중을 견디는게 있으면 그거 하나만 연결하면 된다!!
print(max(w))
