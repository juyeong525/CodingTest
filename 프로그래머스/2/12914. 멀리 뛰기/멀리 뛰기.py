def solution(n):
    v = [0,1,2,3] + [0] * n
    for i in range(4, n+1):
        v[i] = (v[i-2] + v[i-1]) % 1234567
    return v[n]