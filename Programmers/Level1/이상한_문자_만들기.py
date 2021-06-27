def solution(s):
    answer = ''
    ch = -1
    for x in s:
        ch += 1
        if x == ' ':
            answer += x
            ch = -1
        else:
            if ch % 2 == 0:
                answer += x.upper()
            else:
                answer += x.lower()
    return answer