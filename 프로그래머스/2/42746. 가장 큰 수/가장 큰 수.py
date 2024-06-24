def solution(numbers):
    numbers = list(map(str, numbers)) # join 사용하기 위해 str으로 mapping
    numbers.sort(reverse=True, key= lambda x: x * 5) # 4을 곱해줌으로써 1의 자리수 
    if "".join(numbers).replace("0","") == "":
        return "0"
    else:
        return "".join(numbers)