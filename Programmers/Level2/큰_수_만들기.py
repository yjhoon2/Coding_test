# 시간초과
from itertools import combinations
def solution(number, k):
    n = len(number) - k
    lst = list(combinations(number, n))
    ans = 0
    for num in lst:
        if int(''.join(num)) > ans:
            ans = int(''.join(num))
    return str(ans)

# 내 풀이
def solution(number, k):
    ans = []
    for idx, num in enumerate(number):
        if k == 0:
            ans.append(number[idx:])
            break
            
        if len(ans) == 0:
            ans.append(num)
        else:
            while ans and ans[-1] < num and k > 0:
                ans.pop()
                k -= 1
            ans.append(num)
    
    if k != 0:
        while k > 0:
            ans.pop()
            k -= 1
    
    return ''.join(ans)
    
# 비슷한 풀이인데 더 정리가 잘 되어 있음
def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)