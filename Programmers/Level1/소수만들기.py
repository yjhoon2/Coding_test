import itertools

def solution(nums):
    l = list(itertools.combinations(nums, 3))
    
    answer = 0
    for i in range(len(l)):
        check = 0
        num = sum(l[i])
        for j in range(2, num//2 + 1):
            if num%j == 0:
                check += 1
        if check == 0:
            answer += 1
                
    return answer