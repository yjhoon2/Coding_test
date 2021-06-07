def solution(s):
    n = len(s)
    k = n//2
    if n%2 == 0:
        answer = s[k-1:k+1]
    else:
        answer = s[k]
    return answer