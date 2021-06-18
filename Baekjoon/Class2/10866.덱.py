import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline


from collections import deque
import sys

t = int(input())
Q = deque()
res = []

L = sys.stdin.read().splitlines()
for idx in range(t):
    a,*b = L[idx].split()
    if "push_front" in a:
        Q.appendleft(b[0])
    elif "push_back" in a:
        Q.append(b[0])
    elif a == "pop_front":
        res.append(Q.popleft() if Q else "-1")
    elif a == "pop_back":
        res.append(Q.pop() if Q else "-1")
    elif a == "size":
        res.append(str(len(Q)))
    elif a == "empty":
        res.append('0' if Q else "1")
    elif a == "front":
        res.append(Q[0] if Q else "-1")
    elif a == "back":
        res.append(Q[-1] if Q else "-1")
print("\n".join(res))