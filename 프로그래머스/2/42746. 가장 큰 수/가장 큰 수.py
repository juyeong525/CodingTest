from itertools import combinations, permutations

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True, key= lambda x: x * 4)
    if "".join(numbers).replace("0","") == "":
        return "0"
    else:
        return "".join(numbers)