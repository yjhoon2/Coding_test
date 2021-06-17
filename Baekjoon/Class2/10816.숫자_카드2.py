import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

import sys
n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# hash 자료구조 이용
hash = dict()
for x in cards:
    if x in hash:
        hash[x] += 1   
    else:
        hash[x] = 1

for y in arr:
    if y in hash:
        print(hash[y], end = ' ')
    else:
        print(0, end = ' ')

# 아래 방법은 시간초과...
'''
for x in arr:
    print(cards.count(x), end = ' ')'''