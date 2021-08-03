def solution(n, results):
    answer = 0
    winners , losers = {}, {}
    
    for i in range(1, n+1):
        winners[i] = set()
        losers[i] = set()
        
    for x in results:
        winners[x[0]].add(x[1])
        losers[x[1]].add(x[0])
        
    for j in range(1, n+1):
        for w in losers[j]:
            winners[w].update(winners[j])
        for l in winners[j]:
            losers[l].update(losers[j])
    
    for a in range(1, n+1):
        if len(winners[a]) + len(losers[a]) == n-1:
            answer += 1
        
    return answer