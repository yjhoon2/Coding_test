def solution(nums):
    a = list(set(nums))
    if len(a) > (len(nums)//2):
        answer = len(nums)//2
    else:
        answer = len(a)
    
    return answer