from itertools import permutations
def solution(numbers):
    lst = []
    for i in range(1, len(numbers)+1):
        lst.extend(list(permutations(numbers,i)))
    
    nums = []
    for i in range(len(lst)):
        num = int(''.join(lst[i]))
        nums.append(num)
    nums = list(set(nums))
    
    cnt = 0
    for x in nums:
        if x > 1:
            for j in range(2, x//2 + 1):
                if x % j == 0:
                    break
            else:
                cnt += 1
    return cnt


# 다른사람의 풀이

from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)