def solution(n, arr1, arr2):
    list = [2 ** a for a in range(n-1,-1,-1)]
    answer = [" " * n for _ in range(n)]
    answer1 = []
    answer2 = []
    for i in arr1:
        v = ""
        for j in range(len(list)):
            if i >= list[j]:
                v += "#"
                i -= list[j]
            else:
                v += " "
        answer1.append(v)
    for i in arr2:
        v = ""
        for j in range(len(list)):
            if i >= list[j]:
                v += "#"
                i -= list[j]
            else:
                v += " "
        answer2.append(v)
    print(answer1)
    print(answer2)
    for i in range(n):
        w = ""
        for k in range(n):
            if "#" in set(answer1[i][k]) | set(answer2[i][k]):
                w += "#"
            else:
                w += " "
        answer[i] = w
    print(answer)
    return answer