def solution(brown, yellow):
    blocks = brown + yellow
    lst = []
    for i in range(2, blocks//2+1):
        if blocks % i == 0:
            lst.append((blocks//i, i))
    
    for l in lst:
        if l[0]*2 + (l[1]-2)*2 == brown:
            return [l[0], l[1]]