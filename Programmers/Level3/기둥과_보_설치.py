##### 노가다 1 실패
def solution(n, build_frame):
    answer = []
    for build in build_frame:
        x, y, a, b = build
        if b == 1:
            if a == 0:
                if y == 0 or ([x-1, y, 1] in answer) or ([x+1, y, 1] in answer) or ([x, y-1, 0] in answer):
                    answer.append([x, y, a])
            if a == 1:
                if ([x, y-1, 0] in answer) or ([x+1, y-1, 0] in answer) or (([x-1, y, 1] in answer) and ([x+1, y, 1] in answer)):
                    answer.append([x, y, a])
        else:
            if [x, y, a] in answer:
                answer.remove([x, y, a])
            for ans in answer:
                xx, yy, aa = ans
                if aa == 0:
                    if yy == 0 or ([xx-1, yy, 1] in answer) or ([xx+1, yy, 1] in answer) or ([xx, yy-1, 0] in answer):
                        continue
                    else:
                        answer.append([x, y, a])
                        break
                if aa == 1:
                    if ([xx, yy-1, 0] in answer) or ([xx+1, yy-1, 0] in answer) or (([xx-1, yy, 1] in answer) and ([xx+1, yy, 1] in answer)):
                        continue
                    else:
                        answer.append([x, y, a])
                        break
            
    answer.sort(key = lambda x : (x[0], x[1], x[2]))
    return answer

## 노가다 2 실패
def check(frame):
    for f in frame:
        x, y, a = f
        if a == 0:
            if y == 0 or ([x-1, y, 1] in frame) or ([x+1, y, 1] in frame) or ([x, y-1, 0] in frame):
                continue
            else:
                return False
        else:
            if ([x, y-1, 0] in frame) or ([x+1, y-1, 0] in frame) or (([x-1, y, 1] in frame) and ([x+1, y, 1] in frame)):
                continue
            else:
                return False
    return True
                

def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        build = (x, y, a)
        if b == 0:
            answer.append(build)
            if check(answer) == False:
                answer.remove(build)
        else:
            if build in answer:
                answer.remove(build)
                if check(answer) == False:
                    answer.append(build)
    
    answer.sort(key = lambda x : (x[0], x[1], x[2]))
    return answer


### 다른넘 풀이
def impossible(result):
    COL, ROW = 0, 1
    for x, y, a in result:
        if a == COL: # 기둥일 때
            if y != 0 and (x, y-1, COL) not in result and \
        (x-1, y, ROW) not in result and (x, y, ROW) not in result:
                return True
        else: # 보일 때
            if (x, y-1, COL) not in result and (x+1, y-1, COL) not in result and \
        not ((x-1, y, ROW) in result and (x+1, y, ROW) in result):
                return True
    return False

def solution(n, build_frame):
    result = set()
    
    for x, y, a, build in build_frame:
        item = (x, y, a)
        if build: # 추가일 때
            result.add(item)
            if impossible(result):
                result.remove(item)
        elif item in result: # 삭제할 때
            result.remove(item)
            if impossible(result):
                result.add(item)
    answer = map(list, result)
    
    return sorted(answer, key = lambda x : (x[0], x[1], x[2]))