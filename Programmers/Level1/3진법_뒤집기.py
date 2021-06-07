# 내 풀이
def solution(n):
    k = 0
    while 3**(k+1) <= n:
        k += 1
    
    three = ''
    for i in range(k, -1, -1):
        three = three + str(n//(3**i))
        n = n%(3**i)
        if n == 0:
            break
    
    three = three[::-1]
    answer = 0
    for j in range(len(three)):
        answer += int(three[-1-j])*(3**j)
    
    return answer

# 다른사람 풀이
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer