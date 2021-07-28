# 와 이거 힙은 내 혼자 못풀겠다...
import heapq
def solution(jobs):
    answer = 0
    start = -1
    now = 0
    i = 0
    hq = []
    
    while i < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(hq, [job[1], job[0]])
        if hq:
            a = heapq.heappop(hq)
            start = now
            now += a[0]
            answer += now - a[1]
            i += 1
        else:
            now += 1
    return answer//len(jobs)