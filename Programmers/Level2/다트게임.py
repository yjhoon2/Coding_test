# 내 풀이
def solution(dartResult):
    a = []
    num = 0
    for i in range(len(dartResult)):
        if dartResult[i] == '0' and dartResult[i-1] in list(map(str, range(1, 10))): 
            continue
        if dartResult[i] in list(map(str, range(10))):
            a.append(num)
            num = 0
            if dartResult[i+1] == '0':
                num = int(dartResult[i:i+2])
            else:
                num = int(dartResult[i])
                
        if dartResult[i] == "D":
            num = num**2
        elif dartResult[i] == "T":
            num = num**3
              
        if dartResult[i] == '*':
            num = num*2
            if len(a) != 0:
                a[-1] = a[-1]*2
        elif dartResult[i] == '#':
            num = num*(-1)
    else:
        a.append(num)
    
    answer = sum(a)      
                
    return answer

## 다른사람 풀이
# 미쳤다 이건 공부해보자

import re

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)') # () 는 그루핑 해줌. / ? : 있어도 되고 없어도 된다
    dart = p.findall(dartResult) # ex) dartResult = '1D2S#10S' / dart = [('1', 'D', ''), ('2', 'S', '#'), ('10', 'S', '')]
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer

dartResult = '1D2S#10S'
bonus = {'S' : 1, 'D' : 2, 'T' : 3}
option = {'' : 1, '*' : 2, '#' : -1}
p = re.compile('(\d+)([SDT])([*#]?)')
dart = p.findall(dartResult)
print(dart)