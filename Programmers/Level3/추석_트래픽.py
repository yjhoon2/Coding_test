def check(t, li):
    start = t
    end = t + 1000
    cnt = 0
    for i in li:
        if start <= i[1] and end > i[0]:
            cnt += 1
    return cnt

def solution(lines):
    arr = []
    for line in lines:
        y, time, term = line.split()
        time = time.split(":")
        term = float(term.replace("s", '')) * 1000
        end = (3600*int(time[0]) + 60*int(time[1]) + float(time[2]))*1000
        start = end - term + 1
        arr.append([start, end])
        
    res = 0
    for x in arr:
        res = max(res, check(x[0], arr), check(x[1], arr))
        
    return res