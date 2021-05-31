def solution(answers):
    a = [1, 2, 3, 4, 5] # 5
    b = [2, 1, 2, 3, 2, 4, 2, 5] # 8
    c = [3, 3, 1, 1, 2, 2, 4 ,4 ,5, 5] # 10
    supo = [a, b, c]
    
    score = []
    res = 0
    for i, j in enumerate(supo):
        l = len(j)
        max = 0
        for k in range(len(answers)):
            if answers[k] == j[k%l]:
                max += 1
        if max > res:
            res = max
        score.append((i+1, max))
    
    answer = []
    for i in range(len(score)):
        if score[i][1] == res:
            answer.append(score[i][0])
    
    
    return answer