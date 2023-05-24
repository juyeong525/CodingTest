def solution(fees, records):
    inArray = []
    code = []
    result = []
    for record in records:
        r = record.split(" ")
        if r[2] == "IN":
            code.append(r[1])
            time = list(map(int,r[0].split(":")))
            sum = hourToMinute(time[0], time[1])
            inArray.append([sum, r[1]])
        else:
            for i in inArray:
                if i[1] == r[1] and i[0] >= 0:
                    time = list(map(int,r[0].split(":")))
                    sum = hourToMinute(time[0], time[1])
                    i[0] -= sum
                    break
    for i in inArray:
        if i[0] >= 0: 
            i[0] -= hourToMinute(23, 59)
    code = sorted(list(set(code)))
    for c in code:
        count = 0
        for i in inArray:
            if i[1] == c:
                count += i[0]
        print(c ,count)
        if -count <= fees[0]:
            result.append(fees[1])
        else:
            z = ((-count - fees[0]) // fees[2])
            if ((-count - fees[0]) / fees[2]) - z > 0:
                result.append(fees[1]+(z + 1) * fees[3])
            else:
                result.append(fees[1]+ z * fees[3])
    return result

def hourToMinute(hour, minute):
    return hour * 60 + minute
    
