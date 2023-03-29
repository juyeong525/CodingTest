def solution(n):
    v = []
    while(n != 0):
        a = n % 10
        n = n // 10
        v.append(a)
    
    return v