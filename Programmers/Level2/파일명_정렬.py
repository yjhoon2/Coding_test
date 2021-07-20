## 답은 맞는데 런타임 에러남..
def solution(files):
    n = len(files)
    all = []
    for i in range(n):
        file = []
        for j in range(len(files[i])):
            if files[i][j].isdecimal():
                file.append(files[i][:j])
                for k in range(j, len(files[i])):
                    if files[i][k].isdecimal() == False:
                        if len(files[i][j:k]) > 5:
                            file.append(files[i][j:j+5])
                            file.append(files[i][j+5:])
                            break
                        else:
                            file.append(files[i][j:k])
                            file.append(files[i][k:])
                            break
                break
        all.append(file)
    all.sort(key = lambda x : (x[0].lower(), int(x[1])))
    
    answer = []
    for w in all:
        answer.append(''.join(w))
        
    return answer

## 정규표현식 ㅁㅊ...
def solution(files):
    import re
    all = [re.split(r'([0-9]+)', s) for s in files]
    all.sort(key = lambda x : (x[0].lower(), int(x[1])))
        
    return [''.join(w) for w in all]