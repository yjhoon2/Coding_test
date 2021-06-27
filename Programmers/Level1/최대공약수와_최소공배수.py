def solution(n, m):
    x = max(n, m)
    y = min(n, m)

    # 유클리드 호제법
    while x % y != 0:
        x, y = y, x%y
    return [y, n*m//y]