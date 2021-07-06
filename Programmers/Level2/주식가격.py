def solution(prices):
    answer = [0]*len(prices)
    stack = []
    for idx, prc in enumerate(prices):
        if len(stack) == 0:
            stack.append((idx, prc))
        else:
            if stack[-1][1] <= prc:
                stack.append((idx, prc))
            else:
                jj = stack.pop()
                answer[jj[0]] = (idx - jj[0])
                while stack and stack[-1][1] > prc:
                    j = stack.pop()
                    answer[j[0]] = idx - j[0]
                stack.append((idx, prc))
    for i in range(len(stack)):
        k = stack.pop()
        answer[k[0]] = len(prices)-1-k[0]
    return answer