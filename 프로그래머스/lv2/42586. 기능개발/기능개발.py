import math
def solution(progresses, speeds):
    count = 0
    works = []
    n = []
    a = math.ceil((100 - progresses[0]) / speeds[0])
    for i in range(len(progresses)):
        if a >= math.ceil((100 - progresses[i]) / speeds[i]):
            count += 1
        else:
            a = math.ceil((100 - progresses[i]) / speeds[i])
            n.append(count)
            count = 1
        works.append(math.ceil((100 - progresses[i]) / speeds[i]))
    print(works)
    n.append(count)
    return n