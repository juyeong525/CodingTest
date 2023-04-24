def solution(N, stages):
    stage = sorted(stages)
    answer = []
    result = []
    for i in range(1, N+1):
        count = 0
        for j in stage:
            if i == j:
                count+=1
            else:
                break
        if len(stage) != 0:
            answer.append(count / len(stage))
        else:
            answer.append(0)
        stage = stage[count:]
    index = list(enumerate(answer, start=1))
    answer = sorted(answer)
    for i in index:
        for j in range(len(index)):
            if max(answer) == index[j][1] and index[j][0] not in result:
                result.append(index[j][0])
                answer.pop(-1)
                break
    return result