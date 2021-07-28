def solution(n, computers):
    ch = [0]*n
    cnt = 0
    def DFS(start):
        nonlocal cnt
        ch[start] = 1
        for i in range(n):
            if ch[i] == 0 and computers[start][i] == 1:
                DFS(i)
                    
    for i in range(n):
        if ch[i] == 0:
            DFS(i)
            cnt += 1
    return cnt