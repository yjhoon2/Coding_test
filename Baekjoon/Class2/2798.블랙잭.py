import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

from itertools import combinations
nums = list(combinations(arr, 3))
max = 0
for x in nums:
    if sum(x) <= m and max < sum(x):
        max = sum(x)
print(max)