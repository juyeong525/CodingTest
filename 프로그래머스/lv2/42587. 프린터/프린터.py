def solution(priorities, location):
    answer = []
    index = []
    n = []
    for i in range(len(priorities)):
        n.append(i)
    while(len(priorities) != 0):
        count = len(priorities) 
        key = priorities.pop(0)
        key1 = n.pop(0)
        for i in priorities:
            if key < i:
                priorities.append(key)
                n.append(key1)
                break
        if count != len(priorities):
            answer.append(key)
            index.append(key1)
    print(answer)
    print(index)
    return index.index(location)+1