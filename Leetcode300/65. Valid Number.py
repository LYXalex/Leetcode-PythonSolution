class Solution:
    # 一个.或者没有.
    # 一个E,e 或者没有(e后可以跟一个+,-)
    # 开头可以用一个加号减号
    def isNumber(self, s: str) -> bool:
        if s[0] != "." and s[0] != "+" and s[0] != "-" and not s[0].isdigit(): return False
        dot = False
        hasE = False
        if s[0] == ".": dot = True
        digit = False
        if s[0].isdigit(): digit = True
        i = 1
        while i < len(s):
            if s[i].isdigit():
                digit = True
                i += 1
            elif digit and not hasE and (s[i] == "e" or s[i] == "E"):
                hasE = True
                dot = True
                if i + 1 >= len(s): return False
                i += 1
                if s[i].isdigit():
                    i += 1
                elif s[i] == "+" or s[i] == "-":
                    i += 1
                    if i >= len(s):
                        return False
                    elif s[i].isdigit():
                        i += 1
                    else:
                        return False
                else:
                    return False
            elif not dot and s[i] == ".":
                dot = True
                i += 1
            else:
                return False
        return True if digit else False


