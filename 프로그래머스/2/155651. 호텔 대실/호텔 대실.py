def solution(book_time):
    book_int_time = map(toM, book_time)
    stack = []
    
    for i in sorted(book_int_time):
        stack.sort(reverse=True, key = lambda x: x[1])
        if len(stack) != 0 and stack[-1][1] + 10 <= i[0] :
            stack.pop()
        stack.append(i)
    return len(stack)

def toM(l):
    result = []
    for i in l:
        h, m = i.split(":")
        result.append(int(h) * 60 + int(m))
    return result