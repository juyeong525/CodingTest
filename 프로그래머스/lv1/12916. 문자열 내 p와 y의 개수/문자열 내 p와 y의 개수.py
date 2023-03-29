def solution(s):
    answer = ""
    pcount = 0
    ycount = 0
    for i in s:
        i = i.upper()
        answer = answer + i
    for j in answer:
        if j == "P":
            pcount += 1
        elif j == "Y":
            ycount += 1
        else:
            pass
    
    return pcount == ycount