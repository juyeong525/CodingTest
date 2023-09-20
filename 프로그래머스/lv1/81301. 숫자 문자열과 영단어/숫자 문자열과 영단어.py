def solution(s):
    list = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    answer = ""
    result = ""
    for i in s:
        result += i
        if result.isdigit():
            answer += result
            result = ""
        elif result in list:
            answer += str(list.index(result))
            result = ""
    return int(answer)