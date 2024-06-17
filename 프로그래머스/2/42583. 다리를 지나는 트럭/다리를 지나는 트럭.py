from collections import deque
def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    current_truck = deque([0 for _ in range(bridge_length)])
    count = 0
    sum_current = 0
    while truck_weights:
        sum_current -= current_truck.popleft()
        sum_current += truck_weights[0]
        if sum_current <= weight:
            current_truck.append(truck_weights.popleft())
        else:
            sum_current -= truck_weights[0]
            current_truck.append(0)
        count += 1
    return count + bridge_length