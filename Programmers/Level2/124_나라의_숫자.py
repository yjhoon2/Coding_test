def solution(n):
    answer = ''
    aa = ['1', '2', '4']
    while True:
        if n <= 3:
            answer += aa[n-1]
            break
        else:
            a = (n-1)%3
            n = (n-1)//3 
            answer += aa[a]
    answer = answer[::-1]
    return answer