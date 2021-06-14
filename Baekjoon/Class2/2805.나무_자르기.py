import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

lt = 0
rt = max(trees)

while lt <= rt:
    cut = (lt+rt)//2
    take = 0
    for x in trees:
        if x > cut:
            take += x-cut
    if take > m:
        res = cut
        lt = cut+1
    else:
        rt = cut-1

print(res)