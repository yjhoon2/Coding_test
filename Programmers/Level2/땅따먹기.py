# DFS로 풀었는데 시간초과 + 런타임에러...
def solution(land):
    res = 0
    
    def DFS(x, y, yy, sum):
        nonlocal res
        if y == yy:
            return
        if x == len(land):
            if sum > res:
                res = sum
            return
        else:
            DFS(x+1, 0, y, sum + land[x][y])
            DFS(x+1, 1, y, sum + land[x][y])
            DFS(x+1, 2, y, sum + land[x][y])
            DFS(x+1, 3, y, sum + land[x][y])
    
    DFS(0, 0, 4, 0)
    DFS(0, 1, 4, 0)
    DFS(0, 2, 4, 0)
    DFS(0, 3, 4, 0)

    return res


# 다이나믹 프로그래밍...
def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
            
    return max(land[-1])