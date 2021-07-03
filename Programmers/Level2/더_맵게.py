def solution(scoville, K):
    import heapq as hq
    hq.heapify(scoville)
    cnt = 0
    while True:
        if scoville[0] >= K:
            break
        else:
            if len(scoville) <= 1:
                cnt = -1
                break
            else:
                a = hq.heappop(scoville)
                b = hq.heappop(scoville)
                c = a + b*2
                hq.heappush(scoville, c)
                cnt += 1
    return cnt