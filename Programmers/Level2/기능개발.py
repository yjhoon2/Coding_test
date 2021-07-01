from collections import deque
def solution(progresses, speeds):
    q1 = deque(progresses)
    q2 = deque(speeds)
    answer = []
    while q1:
        q1 = deque(x+y for x, y in zip(q1, q2))
        cnt = 0
        if q1[0] >= 100:
            while len(q1) != 0 and q1[0] >= 100:
                cnt += 1
                q1.popleft()
                q2.popleft()
            answer.append(cnt)
    return answer