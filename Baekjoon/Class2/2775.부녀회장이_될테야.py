import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    k = int(input())
    m = int(input())
    last = [x for x in range(1, m+1)]
    now = [0]*m
    for i in range(k):
        for j in range(m):
            now[j] = sum(last[:j+1])
        if i != k-1:
            now, last = last, now
    print(now[m-1])
