def solution(d, budget):
    answer = sorted(d)
    a = 0
    count = 0
    for i in answer:
        if a + i> budget:
            break
        a += i
        count += 1
    return count