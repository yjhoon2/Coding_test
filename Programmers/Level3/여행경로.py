from collections import defaultdict
def solution(tickets):
    answer = []
    route = defaultdict(list)
    for key, value in tickets:
        route[key].append(value)
    for r in route:
        route[r].sort(reverse=True)
    
    stack = ["ICN"]
    path = []
    
    while stack:
        top = stack[-1]
        if top not in route or len(route[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(route[top].pop())
    return path[::-1]