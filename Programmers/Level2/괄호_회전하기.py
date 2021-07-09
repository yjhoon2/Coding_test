from collections import deque
def solution(s):
    Q = deque()
    for x in s:
        Q.append(x)
    
    cnt = 0
    
    for _ in range(len(Q)):
        Q.append(Q.popleft())
        stack = []
        for z in Q:
            if len(stack) == 0:
                stack.append(z)
            else:
                if stack[-1] == '[' and z == ']':
                    stack.pop()
                elif stack[-1] == '{' and z == '}':
                    stack.pop()
                elif stack[-1] == '(' and z == ')':
                    stack.pop()
                else:
                    stack.append(z)
        if len(stack) == 0:
            cnt += 1
    return cnt
    