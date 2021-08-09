import heapq as hq
def solution(operations):
    heap = []
    for op in operations:
        a, b = op.split()
        if a == 'I':
            hq.heappush(heap, int(b))
        elif a == "D" and b == "1" and len(heap) != 0:
            heap.remove(max(heap))
        elif a == "D" and b == "-1" and len(heap) != 0:
            hq.heappop(heap)
    
    if len(heap) == 0:
        return [0,0]
    else:
        return [max(heap),hq.heappop(heap)]