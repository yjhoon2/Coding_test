# 테케 1번만 런타임에러
def solution(n):
    memo = [0] * (n+1)
    memo[1] = 1
    memo[2] = 2
    for i in range(3, n+1):
        memo[i] = memo[i-2] + memo[i-1]
    return memo[n]%1234567

# 이번엔 그냥 실패
def solution(n):
    a, b = 1, 2
    for _ in range(n-2):
        b, a = a+b, b
    return b % 1234567

# n이 1인 경우라네 ㅋㅋㅋㅋ
def solution(n):
    if n < 3:
        return n
    a, b = 1, 2
    for _ in range(n-2):
        b, a = (a+b), b
    return b % 1234567