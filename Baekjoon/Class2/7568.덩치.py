import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

for i in range(n):
    cnt = 1
    ch = [0]*n
    ch[i] = 1
    for j in range(n):
        if ch[j] == 0 and arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            cnt += 1
    print(cnt, end = ' ')