# 내 풀이
# 이거 왜 틀렸는지 아시는 분...

def solution(N, stages):
    rate = []
    m = len(stages)
    for i in range(1, N+1):
        if m == 0:
            rate.append((i, 0))
        else:
            n = stages.count(i)
            rate.append((i, 1 - n/m))
            m -= n
        
    rate.sort(key = lambda x : (x[1], x[0]))
    answer = []
    for i in range(len(rate)):
        answer.append(rate[i][0])
    
    return answer


# 다른 사람 풀이
def solution(N, stages):
    rate = {}
    m = len(stages)
    for i in range(1, N+1):
        if m == 0:
            rate[i] = 0
        else:
            n = stages.count(i)
            rate[i] = n/m
            m -= n 
    
    return sorted(rate, key = lambda x : rate[x], reverse = True)