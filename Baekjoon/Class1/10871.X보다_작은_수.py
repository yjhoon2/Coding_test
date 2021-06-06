import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
'''
n, x = map(int, input().split())
num = list(map(int, input().split()))

for i in num:
    if i < x:
        print(i, end = ' ')
'''
# 이것도 참고
n = int(input().split()[1])
print(' '.join(x for x in input().split() if int(x) < n))