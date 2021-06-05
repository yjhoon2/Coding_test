def solution(left, right):
    answer = 0
    sq = [k**2 for k in range(1, 32)]
    for i in range(left, right+1):
        if i in sq:
            answer -= i
        else:
            answer += i
    return answer