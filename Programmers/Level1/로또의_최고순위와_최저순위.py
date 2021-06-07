def solution(lottos, win_nums):
    lottos.sort()
    win_nums.sort()
    
    zeros = 0
    lucky = 7
    for i in range(len(lottos)):
        if lottos[i] == 0:
            zeros += 1
        elif lottos[i] in win_nums:
            lucky -= 1
    
    if lucky == 7:
        lucky = 6
    
    answer = [lucky - zeros, lucky]
    
    if zeros == 6:
        answer = [1, 6]
    
    return answer