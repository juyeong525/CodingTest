def solution(book_time):
    book_int_time = []
    for book in book_time:
        book_int = []
        for b in book:
            book_int.append(toM(b))
        book_int_time.append(book_int)
    stack = []
    
    for i in sorted(book_int_time):
        stack.sort(reverse=True, key = lambda x: x[1])
        if len(stack) == 0:
            stack.append(i)
        else:
            if stack[-1][1] + 10 > i[0]:
                stack.append(i)
            else:
                stack.pop()
                stack.append(i)
    return len(stack)

def toM(string):
    h, m = string.split(":")
    return int(h) * 60 + int(m)