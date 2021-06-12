import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

ch = [0]*(max(nums)+1)
cnt = 0

for i in range(2, max(nums) + 1):
    if ch[i] == 0:
        if i in nums:
            cnt += 1
        for j in range(i, max(nums)+1, i):
            ch[j] = 1
print(cnt)