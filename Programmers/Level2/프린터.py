from collections import deque
def solution(priorities, location):
    Q = deque()
    for idx, imp in enumerate(priorities):
        Q.append((idx, imp))
    ord = 0
    while True:
        ch = Q.popleft()
        for x in Q:
            if x[1] > ch[1]:
                Q.append(ch)
                break
        else:
            ord += 1
            if ch[0] == location:
                break
    return ord