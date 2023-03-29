def solution(n):
    v = []
    for i in range(1,n+1):
        if n % i == 1:
            v.append(i)
    answer = min(v)
    return answer