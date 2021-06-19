import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

# 이걸로 하면 시간 : 4520ms
n = int(input())
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))
arr.sort(key = lambda x : (x[1], x[0]))

for i in range(n):
    print(arr[i][0], arr[i][1])

# 이걸로 하면 시간 : 376ms
import sys
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    arr.append((x, y))
arr.sort(key = lambda x : (x[1], x[0]))

for i in range(n):
    print(arr[i][0], arr[i][1])