import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    h, w, m = map(int, input().split())
    a = m//h + 1
    b = m%h
    if b == 0:
        b = h
        a -= 1
    print(b*100 + a)