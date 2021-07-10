def solution(dirs):
    points = []
    dict = {'U' : (0, 1), 'D' : (0, -1), 'R' : (1, 0), 'L' : (-1, 0)}
    cnt = 0
    start = (0, 0)
    for d in dirs:
        x, y = start[0] + dict[d][0], start[1] + dict[d][1]
        if -5 <= x <= 5 and -5 <= y <= 5:
            if (start[0], start[1], x, y) not in points:
                points.append((start[0], start[1], x, y))
                points.append((x, y, start[0], start[1]))
                cnt += 1
            start = (x, y)
        
    return cnt