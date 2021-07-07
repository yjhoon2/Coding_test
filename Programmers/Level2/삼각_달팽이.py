def solution(n):
    triangle = [[0]*(i+1) for i in range(n)]
    num = 1
    x, y = -1, 0
    for i in range(n):
        for j in range(i, n):
            if i%3 == 0:
                x += 1
            elif i%3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            triangle[x][y] = num
            num += 1
    
    answer = []
    for i in range(n):
        answer.extend(triangle[i])
                
    return answer