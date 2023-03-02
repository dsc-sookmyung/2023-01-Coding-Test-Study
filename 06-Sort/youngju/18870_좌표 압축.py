import sys

read = sys.stdin.readline
n = int(read())
xlist = list(map(int, read().strip().split()))
xSetList = sorted(set(xlist))
xDict = {}
for i in range(len(xSetList)):
    xDict[xSetList[i]] = i

for j in xlist:
    print(xDict[j], end=" ")
