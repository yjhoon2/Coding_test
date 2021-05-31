def solution(participant, completion):
    p = dict()
    for i in participant:
        p[i] = p.get(i, 0) + 1
    
    for j in completion:
        p[j] -= 1
    
    for key, value in p.items():
        if value != 0:
            answer = key
        
    #answer = ''
    return answer