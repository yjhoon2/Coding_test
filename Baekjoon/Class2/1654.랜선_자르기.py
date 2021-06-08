import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

k, n = map(int, input().split())
lines = []
for _ in range(k):
    lines.append(int(input()))

lt = 1
rt = max(lines)

def Count(l):
    result = 0
    for line in lines:
        result += line // l
    return result

while lt <= rt:
    l = (lt+rt)//2
    if Count(l) >= n:
        res = l
        lt = l+1
    else:
        rt = l-1

print(res)