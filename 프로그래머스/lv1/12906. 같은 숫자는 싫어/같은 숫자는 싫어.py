def solution(arr):
    answer = []
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            arr[i] = ""
    for j in arr:
        if j != "":
            answer.append(j)
    return answer
        