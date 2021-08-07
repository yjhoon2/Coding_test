# 이거 answer 인식 못하는 이유 아는사람??
def DFS(n, m):
    global answer
    if n < m:
        return
    if n == m:
        answer += 1
        return
    DFS(n, m+1)
    DFS(n, m+2)
    return
    

def solution(n):
    answer = 0
    DFS(n, 0)
    return answer

# 일단 위에거 안되길래 이렇게 했는데 테스트케이스만 맞고 채점하면 싹 다 런타임 에러..
def solution(n):
    answer = 0
    def DFS(n, m):
        nonlocal answer
        if n < m:
            return
        if n == m:
            answer += 1
            return
        DFS(n, m+1)
        DFS(n, m+2)
        return
    DFS(n, 0)
    return answer

# 질문하기에 테스트케이스 보다가 규칙찾음 ㅋㅋㅋ 
# 근데 왜인지는 모름
def solution(n):
    a, b = 1, 2
    answer = 2
    while answer < n:
        b, a = a+b, b
        answer += 1
    return b % 1000000007