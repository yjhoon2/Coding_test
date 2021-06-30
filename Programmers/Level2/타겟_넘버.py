def DFS(i, sum, numbers, target):
    global cnt
    if i == len(numbers):
        if sum == target:
            cnt += 1
        return
    else:
        DFS(i+1, sum + numbers[i], numbers, target)
        DFS(i+1, sum - numbers[i], numbers, target)
        
cnt = 0        
def solution(numbers, target):
    DFS(0, 0, numbers, target)
    return cnt

# 이거 왜 안되는지 설명해줄 수 있는 사람?
def DFS(i, sum):
    global cnt
    if i == len(numbers):
        if sum == target:
            cnt += 1
        return
    else:
        DFS(i+1, sum + numbers[i])
        DFS(i+1, sum - numbers[i])
        
cnt = 0        
def solution(numbers, target):
    DFS(0, 0)
    return cnt