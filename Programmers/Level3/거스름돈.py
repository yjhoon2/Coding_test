# 메모이제이션 쓰는건 알았는데 코인별로 할 줄은 몰랐다...

def solution(n, money):
    memo = [1] + [0] * n
    
    for coin in money:
        for i in range(coin, n+1):
            if i >= coin:
                memo[i] += memo[i-coin]
    return memo[n]