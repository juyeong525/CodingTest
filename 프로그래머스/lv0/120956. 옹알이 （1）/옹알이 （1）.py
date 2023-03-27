def solution(babbling):
    answer = 0
    for i in range(len(babbling)):
        for j in ["aya","ye","woo","ma"]:
            babbling[i] = babbling[i].replace(j," ",1)
    for k in babbling:
        p = k.replace(" ","",15)
        if p == "":
            answer+=1
    return answer