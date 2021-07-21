from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque([0]*bridge_length)
    truck_weights = deque(truck_weights)
    bridge_weight = 0
    cnt = 0
    while True:
        bridge_weight -= bridge.popleft()
        if truck_weights and bridge_weight+truck_weights[0] <= weight:
            cnt += 1
            bridge_weight += truck_weights[0]
            bridge.append(truck_weights.popleft())
        elif truck_weights and bridge_weight+truck_weights[0] > weight:
            cnt += 1
            bridge.append(0)
        elif len(truck_weights) == 0:
            cnt += 1
            bridge.append(0)
        
        if bridge_weight == 0 and len(truck_weights) == 0:
            break
    return cnt