def solution(n,a,b):
    answer = 0
    while True:
        q, r = divmod(a, 2)
        a = q+r
        q, r = divmod(b, 2)
        b = q+r
        answer += 1
        if a == b:
            break
    return answer