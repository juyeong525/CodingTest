from collections import deque
def solution(sequence, k):
    start = 0
    end = 0
    s = 0
    result = []
    
    while True:

        if s > k:
            s -= sequence[start]
            start += 1
        elif end == len(sequence):
            s -= sequence[start]
            start += 1
        else:
            s += sequence[end]
            end += 1
        
        if end == len(sequence) and start == len(sequence):
            # print(result)
            result.sort(key=lambda x : (x[1] - x[0], x[0]))
            return result[0]
        
        if s == k:
            result.append([start, end - 1])