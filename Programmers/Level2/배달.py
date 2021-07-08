def solution(N, road, K):
    board = [[500000]*N for _ in range(N)]
    for r in road:
        a, b, c = r
        if board[a-1][b-1] > c: # 똑같은 길에 두가지 시간이 주어질 경우가 있음
            board[a-1][b-1] = c
            board[b-1][a-1] = c
    
    for i in range(N):
        board[i][i] = 0
    
    # 플로이드 와샬 알고리즘
    for k in range(N):
        for i in range(N):
            for j in range(N):
                board[i][j] = min(board[i][j], board[i][k] + board[k][j])
    
    cnt = 0
    for x in board[0]:
        if x <= K:
            cnt += 1

    return cnt