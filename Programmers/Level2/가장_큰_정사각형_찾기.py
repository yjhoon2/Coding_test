def solution(board):
    ch = [[0]*len(board[0]) for _ in range(len(board))]
    ch[0] = board[0]
    for k in range(len(board)):
        ch[k][0] = board[k][0]
    
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                ch[i][j] = min(ch[i-1][j-1], ch[i-1][j], ch[i][j-1]) + 1
                    
    ans = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if ans < ch[i][j]:
                ans = ch[i][j]
                
    return ans**2