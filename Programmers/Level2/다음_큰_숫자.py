def solution(n):
    num = bin(n)
    m = num.count("1")
    n += 1
    while bin(n).count("1") != m:
        n += 1
    return n