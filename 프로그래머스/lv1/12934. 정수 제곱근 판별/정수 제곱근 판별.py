def solution(n):
    answer = 0
    for i in range(1, n+1):
        if i*i == n:
            answer = (i+1) * (i+1)
            break
        else:
            answer = -1
    return answer