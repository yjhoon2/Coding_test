import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

a, b, v = map(int, input().split())

cnt = (v-a)//(a-b)
k = (v-a)%(a-b)
if k == 0:
    print(cnt + 1)
else:
    print(cnt + 2)
