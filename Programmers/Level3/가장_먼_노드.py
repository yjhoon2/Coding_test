def solution(n, edge):
    board = [[0]*(n+1) for _ in range(n+1)]
    for x in edge:
        a, b = x[0], x[1]
        board[a][b] = 1
        board[b][a] = 1
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                if k != i and k != j:
                    board[i][j] = max(board[i][j], board[i][k]+board[k][j])
        
    return board[1].count(max(board[1]))


## 큐 자료구조 이용해서 푸는거였음...
from collections import deque
def solution(n, edge):
    dict = {}
    for x in edge:
        dict[x[0]] = dict.get(x[0], []) + [x[1]]
        dict[x[1]] = dict.get(x[1], []) + [x[0]]
        
    q = deque()
    q.append(1)
    ch = [0] * (n+1)
    ch[1] = 1
    while q:
        nodes = len(q)
        for _ in range(nodes):
            a = q.popleft()
            for b in dict[a]:
                if ch[b] == 0:
                    ch[b] = 1
                    q.append(b)
                
    return nodes