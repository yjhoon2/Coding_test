## 이건 혼자 못 품..
answer = []
def DFS(n, start, end, assist):
    global answer
    if n == 1:
        answer.append([start, end])
        return
    else:
        DFS(n-1, start, assist, end)
        answer.append([start, end])
        DFS(n-1, assist, end, start)

def solution(n):
    global answer
    DFS(n, 1, 3, 2)
    return answer