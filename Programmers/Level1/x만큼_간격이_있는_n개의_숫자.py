def solution(x, n):
    if x == 0:
        return [0]*n
    else:
        return list(range(x, x*(n+1), x))