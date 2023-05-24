# 17609 회문
import sys

def secondrun(word,left,right):
    while (left < right):
        if (word[left] == word[right]):
            left += 1
            right -= 1
        else:
            return False
    return True


def findcheck(word,left,right):
    while (left < right):
        if (word[left] == word[right]):
            left += 1
            right -= 1
        else:
            check1 = secondrun(word,left+1,right)
            check2 = secondrun(word,left,right-1)
            if(check1 or check2):
                return 1
            else:
                return 2
    return 0

N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    left=0
    right=len(word)-1
    print(findcheck(word,left,right))
