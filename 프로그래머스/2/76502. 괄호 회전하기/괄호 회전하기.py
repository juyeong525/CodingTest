def solution(s):
    index = 0
    s.replace("[]", "")
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
        # if s.find("(") <= s.find(")") and s.count("(") == s.count(")") and s.find("[") <= s.find("]") and s.count("[") == s.count("]") and s.find("{") <= s.find("}") and s.count("{") == s.count("}"):
        #     index += 1
        s = s[1:] + s[0]
    return index
