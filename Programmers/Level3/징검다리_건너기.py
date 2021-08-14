# 이거하니까 효율성에서 다 떨어짐
def solution(stones, k):
    answer = 0
    while True:
        jump = 0
        for i in range(len(stones)):
            if stones[i] == 0 and jump == k-1:
                return answer
            elif stones[i] == 0:
                jump += 1
            else:
                stones[i] -= 1
                jump = 0
        else:
            answer += 1
    return answer

# 와 이것도 아이디어 괜찮다고 생각했는데 효율성 1개 통과하네;;
def solution(stones, k):
    answer = 0
    jump = []
    for i in range(len(stones)-k+1):
        jump.append(max(stones[i:i+k]))
    return min(jump)

# 리스트 구조에서 시간 줄이려고 이거 했는데도 안됨;;
def solution(stones, k):
    answer = 2147000000
    for i in range(len(stones)-k+1):
        if answer > max(stones[i:i+k]):
            answer = max(stones[i:i+k])
    return answer


#### 질문하기 보니까 이진탐색으로 하라더라
def solution(stones, k):
    rt = max(stones)
    lt = min(stones)
    
    while lt <= rt:
        mid = (lt + rt) // 2
        jump = 0
        for i in range(len(stones)):
            if stones[i] - mid <= 0:
                jump += 1
            else:
                jump = 0
            if jump == k:
                break
        
        if jump < k:
            lt = mid + 1
        else:
            rt = mid -1
        
    return lt

