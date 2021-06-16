def solution(s, n):
    u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    l = 'abcdefghijklmnopqrstuvwxyz'
    answer = ''
    for x in s:
        if x == ' ':
            answer += x
        else:
            if x.islower():
                a = l.index(x)
                b = (a+n) % 26
                answer += l[b]
            else: 
                a = u.index(x)
                b = (a+n) % 26
                answer += u[b]
    return answer