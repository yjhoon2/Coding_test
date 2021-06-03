def solution(d, budget):
    d.sort()
    money = 0
    answer = 0
    for i in range(len(d)):
        money += d[i]
        if money > budget:
            answer = i
            break
        if money == budget:
            answer = i + 1
            break
    else:
        answer = len(d)
    return answer


# 다른사람 풀이 best

def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)