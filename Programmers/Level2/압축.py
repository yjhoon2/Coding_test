def solution(msg):
    answer = []
    dict = {}
    for i in range(1, 27):
        dict[chr(64+i)] = i
    num = 27
    a, b = 0, 0
    while True:
        b += 1
        if b == len(msg):
            answer.append(dict[msg[a:b]])
            break
        if msg[a:b+1] not in dict:
            dict[msg[a:b+1]] = num
            num += 1
            answer.append(dict[msg[a:b]])
            a = b
    return answer