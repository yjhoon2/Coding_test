def solution(n, lost, reserve):
    lost_update = list(set(lost) - set(reserve))
    reserve_update = list(set(reserve) - set(lost))
    
    num_lost = len(lost_update)
            
    for i in lost_update:
        if i-1 in reserve_update:
            reserve_update.remove(i-1)
            num_lost -= 1
        elif i+1 in reserve_update:
            reserve_update.remove(i+1)
            num_lost -= 1
    answer = n - num_lost
    return answer