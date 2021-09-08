def solution(n, s):
    a, b = divmod(s, n)
    answer = [a] * n
    if a == 0:
        return [-1]
    for i in range(b):
        answer[i] += 1
    answer.sort()
    return answer