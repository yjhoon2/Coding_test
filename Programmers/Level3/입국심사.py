def solution(n, times):
    lt, rt = 1, n*max(times)
    
    while lt < rt:
        cnt = 0
        time = (lt+rt)//2
        for x in times:
            cnt += time // x
        
        if cnt >= n:
            rt = time 
        else:
            lt = time + 1
        
    return rt

## 근데 이거하면 2, 6, 7번 틀리더라
# 왜인지 아시는 분
def solution(n, times):
    lt, rt = 1, n*max(times)
    
    while lt < rt:
        cnt = 0
        time = (lt+rt)//2
        for x in times:
            cnt += time // x
        
        if cnt >= n:
            rt = time -1
        else:
            lt = time + 1
        
    return time