def solution(id_list, reports, k):
    s = [0 for _ in range(len(id_list))]
    answers = [[] for _ in range(len(id_list))]
    for report in reports:
        a = report.split(" ")
        answers[id_list.index(a[1])].append(a[0])
    for answer in answers:
        if k <= len(set(answer)):
            for an in set(answer):
                s[id_list.index(an)] += 1
                
    return s