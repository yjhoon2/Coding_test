def solution(routes):
    answer = 0
    routes.sort(key = lambda x : x[1])
    
    return routes