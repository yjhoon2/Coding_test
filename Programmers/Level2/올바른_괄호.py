def solution(s):
    stack = []
    for x in s:
        if len(stack) == 0:
            stack.append(x)
        else:
            if x == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(x)
            else:
                stack.append(x)
    if len(stack) == 0:
        return True
    else:
        return False