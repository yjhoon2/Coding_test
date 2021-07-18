from collections import deque
def solution(skill, skill_trees):
    
    cnt = 0
    for s in skill_trees:
        dq = deque(skill)
        for x in s:
            if x in dq:
                if x != dq.popleft():
                    break
        else:
            cnt += 1
    
    return cnt