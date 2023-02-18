#21918 전구
import sys

n, m = map(int,sys.stdin.readline().split())
lights = list(map(int,sys.stdin.readline().split()))
command = [list(map(int,sys.stdin.readline().split())) for _ in range(m)]


def comm_one(lights,i,x):
    lights[i-1] = x
def comm_two(lights,l,r):
    for i in range(l-1,r):
        if lights[i] ==1:
            lights[i] = 0
        else:
            lights[i] = 1
def comm_three(lights,l,r):
    for i in range(l-1,r):
        lights[i] =0
def comm_four(lights,l,r):
    for i in range(l-1,r):
        lights[i] =1
        
        
for i in range(m):
    case = command[i][0]
    one = command[i][1]
    two = command[i][2]
    if case == 1:
        comm_one(lights,one,two)
    elif case ==2:
        comm_two(lights,one,two)
    elif case ==3:
        comm_three(lights,one,two)
    else:
        comm_four(lights,one,two)

for idx in range(len(lights)):
    print(lights[idx], end =' ')