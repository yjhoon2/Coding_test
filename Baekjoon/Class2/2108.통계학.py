import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()
'''
from collections import Counter

def mode(arr):
    if n == 1:
        return arr[0]
    else:
        num_dict = Counter(arr)
        modes = num_dict.most_common()
        if modes[0][1] == modes[1][1]:
            return modes[1][0]
        else:
            return modes[0][0]

print(round(sum(nums)/n))
print(nums[n//2])
print(mode(nums))
print(nums[-1] - nums[0])
'''


print("%.f"%(sum(nums)/n))

nums.sort()
print(nums[n//2])

from collections import Counter
k=Counter(nums).most_common()


if len(nums) > 1: 
    if k[0][1] == k[1][1]:print(k[1][0]) 
    else : print(k[0][0]) 
else : print(nums[0]) 

print(nums[-1] -  nums[0])