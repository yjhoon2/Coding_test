# math 사용
from math import sqrt
def solution(n):
    if n % sqrt(n) == 0:
        return (sqrt(n)+1)**2
    else:
        return -1

# math 사용안함
def solution(n):
    sqrt = n**(1/2)
    if sqrt % 1 == 0:
        return (sqrt+1)**2
    else:
        return -1