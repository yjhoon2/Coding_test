def DFS(v):
    
    
    
def solution(nodeinfo):
    answer = [[]]
    #nodeinfo.sort(key = lambda x : (-x[1], x[0]))
    info = []
    for i, [x, y] in enumerate(nodeinfo):
        info.append([i+1, x, y])
    info.sort(key = lambda x : (-x[2], x[1]))
    return info