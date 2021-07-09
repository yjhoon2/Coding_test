def solution(places):
    answer = []
    
    dx1 = [-1, 0, 1, 0]
    dy1 = [0, -1, 0, 1]
    dx2 = [1, 1, -1, -1]
    dy2 = [1, -1, 1, -1]
    dx3 = [-2, 0, 2, 0]
    dy3 = [0, -2, 0, 2]
    for k in range(5):
        flag = False
        for i in range(5):
            for j in range(5):
                if places[k][i][j] == 'P':
                    for w in range(4):
                        xx = i+dx1[w]
                        yy = j+dy1[w]
                        if 0 <= xx < 5 and 0 <= yy < 5 and places[k][xx][yy] == 'P':
                            answer.append(0)
                            flag = True
                            break
                    if flag:
                        break
                        
                    for v in range(4):
                        xxxx = i+dx2[v]
                        yyyy = j+dy2[v]
                        if 0 <= xxxx < 5 and 0 <= yyyy < 5 and places[k][xxxx][yyyy] == 'P':
                            if places[k][i][yyyy] == 'O' or places[k][xxxx][j] == 'O':
                                answer.append(0)
                                flag = True
                                break
                    if flag:
                        break
                    
                    for z in range(4):
                        xxx = i+dx3[z]
                        yyy = j+dy3[z]
                        if 0 <= xxx < 5 and 0 <= yyy < 5 and places[k][xxx][yyy] == 'P':
                            if places[k][i+dx1[z]][j+dy1[z]] == 'O':
                                answer.append(0)
                                flag = True
                                break
                    if flag:
                        break
                if flag:
                    break
            if flag:
                break
        else:
            answer.append(1)

    return answer