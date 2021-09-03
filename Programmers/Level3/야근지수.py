# 에러 나올 때마다 해결하는 식으로 짰는데 아닌듯...
def solution(n, works):
    works.sort(reverse = True)
    m = len(works)
    for i in range(m):
        if i == m-1:
            works[i] -= 1
            n -= 1
        else:
            while works[i] >= works[i+1]:
                if n == 0:
                    return sum([x**2 for x in works])
                works[i] -= 1
                n -= 1
    
    if n != 0:
        a, b = divmod(n, m)
        works = [x-a for x in works]
        for k in range(b):
            works[k] -= 1
    
    for k in range(m):
        if works[k] < 0:
            works[k] = 0
            
    return sum([x**2 for x in works])

## 테케 효율성 떨어짐
def solution(n, works):
    while n > 0:
        works.sort(reverse = True)
        if works[0] == 0:
            break
        works[0] -= 1
        n -= 1
    return sum([x**2 for x in works])


# heapq 쓰니까 되는구만 하하
import heapq
def solution(n, works):
    works = [-x for x in works]
    heapq.heapify(works)
    while n > 0:
        work = heapq.heappop(works)
        if work == 0:
            break
        work += 1
        n -= 1
        heapq.heappush(works, work)
    return sum([x**2 for x in works])