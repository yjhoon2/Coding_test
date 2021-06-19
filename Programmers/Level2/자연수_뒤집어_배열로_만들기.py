def solution(n):
    n = str(n)
    n = n[::-1]
    answer = [int(x) for x in n]
    return answer


# 다른사람 풀이
def digit_reverse(n):
    return list(map(int, reversed(str(n)))) # map함수 유용하네