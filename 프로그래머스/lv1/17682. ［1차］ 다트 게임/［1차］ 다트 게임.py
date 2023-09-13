def solution(dartResult):
    answer = []
    count = -1
    for i in range(len(dartResult)):
        dart = dartResult[i]
        if dart.isdigit():
            if dartResult[i+1].isdigit():
                answer.append(10)
                count += 1
            elif i > 0 and dartResult[i-1].isdigit():
                pass
            else:
                answer.append(int(dart))
                count += 1
        else:
            if dart == "S":
                pass
            elif dart == "D":
                answer[count] = answer[count] * answer[count]
            elif dart == "T":
                answer[count] = answer[count]*answer[count]*answer[count]
            elif dart == "*":
                if count != 0:
                    answer[count] *= 2
                    answer[count-1] *= 2
                else:
                    answer[count] *= 2
            elif dart == "#":
                answer[count] *= -1
        print(answer)
        
    return sum(answer)