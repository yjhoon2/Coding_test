def solution(n):
    answer = n
    if n == 0:
        return 0
    for i in range(1, n//2 + 1):
        if n % i == 0:
            answer += i
    return answer