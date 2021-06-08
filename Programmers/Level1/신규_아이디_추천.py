def solution(new_id):
    #1
    new_id = new_id.lower()
    #2
    answer = ''
    for a in new_id:
        if a.isalnum() == True or a in '-_.':
            answer += a
    #3
    while '..' in answer:
        answer = answer.replace('..', '.')
    #4
    if answer[0] == '.' and len(answer) > 1: 
        answer = answer[1:]
    if answer[-1] == '.': 
        answer = answer[:-1]
    #5
    if len(answer) == 0:
        answer = "a"
    #6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.': 
            answer = answer[:-1]
    #6
    if len(answer) < 3:
        while len(answer) < 3:
            answer += answer[-1]
    
    return answer