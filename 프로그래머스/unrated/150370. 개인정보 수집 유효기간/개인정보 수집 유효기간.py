def solution(today, terms, privacies):
    t = []
    a = []
    result = []
    for term in terms:
        t.append(int(term.split(" ")[1]))
        a.append(term.split(" ")[0])
    for i in range(len(privacies)):
        p = privacies[i].split(" ")
        date = plusDeadLine(calculateDate(p[0]), t[a.index(p[1])])
        todayDate = calculateDate(today)
        print(date, todayDate)
        if date - todayDate <= 0:
            result.append(i+1)
    return result

def calculateDate(date):
    year, month, day = map(int, date.split("."))
    return (year * 12 * 28) + (month * 28) + day

def plusDeadLine(date, deadLine):
    return date + (deadLine * 28)
