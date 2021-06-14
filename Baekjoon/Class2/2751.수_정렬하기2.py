import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
for i in sorted(nums):
    sys.stdout.write(str(i)+'\n')


'''
# 시간초과
n = int(input())
nums = [int(input()) for _ in range(n)]
for x in sorted(nums):
    print(x)
'''