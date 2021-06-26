def solution(x):
    n = x
    num = 0
    while x > 0:
        num += x%10
        x = x//10
    if n%num == 0:
        return True
    else:
        return False