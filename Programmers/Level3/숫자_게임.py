# 이거 안되네...ㅋㅋ
def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    for a, b in zip(A, B):
        if b > a:
            answer += 1
    return answer

 # 와 이게 되네
 def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    
    while B and A:
        if A[-1] < B[-1]:
            A.pop()
            B.pop()
            answer += 1
        else:
            A.pop()
    
    return answer   