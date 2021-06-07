def solution(board, moves):
    baguni = []
    answer = 0
    
    for i in moves:
        for j in range(len(board[0])):
            if board[j][i-1] != 0:
                baguni.append(board[j][i-1])
                board[j][i-1] = 0
                break
        if len(baguni) >= 2 and baguni[-1] == baguni[-2]:
            baguni.pop()
            baguni.pop()
            answer += 2
            
            
    
    return answer