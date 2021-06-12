import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

a, b = map(int, input().split())

# 에라토스테네스 체
ch = [0] * (b+1)

for i in range(2, b+1):
    if ch[i] == 0:
        if i >= a:
            print(i)
        for j in range(i, b+1, i):
            ch[j] = 1


'''
def sosu(x):
    for i in range(2, x//2+1):
        if x%i == 0:
            return False
    else:
        return True

for k in range(a, b+1):
    if sosu(k):
        print(k)
        '''