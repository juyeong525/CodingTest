def solution(s):
    index = 0
    for i in range(len(s)):
        a = s
        while True:
            if "()" in a or "[]" in a or "{}" in a:
                a = a.replace("[]", "")
                a = a.replace("()", "")
                a = a.replace("{}", "")
            else:
                if len(a) == 0:
                    index += 1
                break
        s = s[1:] + s[0]
    return index
