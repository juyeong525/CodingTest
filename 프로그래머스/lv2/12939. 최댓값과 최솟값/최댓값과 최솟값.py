def solution(s):
    v = list(map(int, s.split()))
    return str(min(v)) + " " + str(max(v))