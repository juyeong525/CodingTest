def solution(citations):
    answer = 0
    citations.sort()
    start = 0
    end = max(citations)
    mid = 0
    print(citations)
    while start <= end:
        mid = (start + end) // 2
        
        print(start, end, mid)
        count = 0
        for i in range(len(citations)):
            if mid <= citations[i]:
                count = len(citations) - i
                break
        
        if mid <= count:
            start = mid + 1
        else:
            end = mid - 1
    return end