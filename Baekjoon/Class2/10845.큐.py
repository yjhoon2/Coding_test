import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

from sys import stdin
from collections import deque
n = int(stdin.readline())
Q = deque()

for _ in range(n):
    arr = stdin.readline().split()
    if arr[0] == 'push':
        Q.append(int(arr[1]))
    elif arr[0] == 'pop':
        if len(Q) != 0:
            print(Q.popleft())
        else:
            print(-1)
    elif arr[0] == 'size':
        print(len(Q))
    elif arr[0] == 'empty':
        if len(Q) != 0:
            print(0)
        else:
            print(1)
    elif arr[0] == 'front':
        if len(Q) != 0:
            print(Q[0])
        else:
            print(-1)
    elif arr[0] == 'back':
        if len(Q) != 0:
            print(Q[-1])
        else:
            print(-1)


# 다른사람 풀이 시간단축
import sys
t = int(input())
q = []
res = []
L = sys.stdin.read().splitlines()
for idx in range(t):
    a,*b = L[idx].split()
    if "push" in a:
        q.append(b[0])
    elif a == "front":
        res.append(q[0] if q else "-1")
    elif a == "back":
        res.append(q[-1] if q else "-1")
    elif a == "size":
        res.append(str(len(q)))
    elif a == "empty":
        res.append('0' if q else "1")
    elif a == "pop":
        res.append(q.pop(0) if q else "-1")
print("\n".join(res))