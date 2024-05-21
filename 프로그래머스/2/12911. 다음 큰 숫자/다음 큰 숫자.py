def checkNumber(n):
    num = format(n, 'b').replace("0","")
    return len(num)

def solution(n):
    num = checkNumber(n)
    while True:
        n += 1
        if num == checkNumber(n):
            return n