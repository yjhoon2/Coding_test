import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

from collections import deque

k = int(input())

for _ in range(k):
    n, m = map(int, input().split())
    Q = [(idx, val) for idx, val in enumerate(list(map(int, input().split())))]
    Q = deque(Q)
    cnt = 0
    while True:
        a = Q.popleft()
        if any(a[1] < x[1] for x in Q):
            Q.append(a)
        else:
            cnt += 1
            if a[0] == m:
                print(cnt)
                break