# 효율성에서 떨어지는 군..
from itertools import permutations
def solution(n, k):
    num = list(range(1, n+1))
    arr = permutations(num, n)
    return list(arr)[k-1]

