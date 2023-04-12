def solution(prices):
    v = []
    count = 0
    for i in range(len(prices)):
        
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                count += 1
            else:
                count += 1
                break
        v.append(count)
        count = 0
    return v
                