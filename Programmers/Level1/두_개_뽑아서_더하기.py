# 다른 사람 풀이가 더 신박하네... 좋다.
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))



# 내 풀이

import itertools

def solution(numbers):
    l = list(itertools.combinations(numbers, 2))
    s = []
    for i in range(len(l)):
        s.append(l[i][0]+l[i][1])
    answer = list(set(s))
    answer.sort()
    return answer