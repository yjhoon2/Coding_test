def solution(record):
    dic = {}
    answer = []
    for re in record:
        x = re.split()
        if (x[0] == 'Enter') | (x[0] == 'Change'):
            dic[x[1]] = x[2]
    for re in record:
        x = re.split()
        if x[0] == 'Enter':
            answer.append(dic[x[1]] + '님이 들어왔습니다.')
        elif x[0] == 'Leave':
            answer.append(dic[x[1]] + '님이 나갔습니다.')
    
    return answer