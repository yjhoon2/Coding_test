## 냅색 알고리즘으로 풀려 했는데 안되는듯...
def solution(n):
    dis = [0]*(n+1)
    for i in range(1, n+1):
        if dis[i] == 0:
            dis[i] = dis[i-1] + 1
            while True:
                k = i*2
                if k > n:
                    break
                elif k == n:
                    dis[k] = dis[i]
                    break
                else:
                    dis[k] = dis[i]
    return dis[n]

## 규칙 찾아서 풀기
def solution(n):
    cnt = 0
    while n > 0:
        n, b = divmod(n, 2)
        cnt += b
    return cnt