from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])

    dis = [[0]*m for _ in range(n)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    Q = deque()
    maps[0][0] = 0
    Q.append((0, 0))

    while Q: # Q가 비면 멈추도록
        tmp = Q.popleft()
        for i in range(4):
            x = tmp[0] + dx[i]
            y = tmp[1] + dy[i]
            if 0 <= x <= (n-1) and 0 <= y <= (m-1) and maps[x][y] == 1:
                maps[x][y] = 0 # 벽으로 만들어 버리기
                dis[x][y] = dis[tmp[0]][tmp[1]] + 1
                Q.append((x, y))

    if dis[n-1][m-1] == 0:
        return -1
    else:
        return dis[n-1][m-1]+1