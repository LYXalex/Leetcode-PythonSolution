class Solution:
    def myAtoi(self, str: str) -> int:
        s = str.strip()
        if not s: return 0
        MAX, MIN = 2 ** 31 - 1, - 2 ** 31
        built_string = ""
        for k, i in enumerate(s):
            if k == 0 and i != '-' and i != '+' and not i.isnumeric(): return 0
            if k > 0:
                if not i.isnumeric() and (built_string == '-' or built_string == '+'): return 0
                if not i.isnumeric(): break
            built_string += i
        multiplier = 1
        if built_string[0] == '-':
            multiplier = -1
            built_string = built_string[1:]
        elif built_string[0] == '+':
            built_string = built_string[1:]
        if not built_string: return 0
        val = int(built_string) * multiplier
        if val < MIN: return MIN
        if val > MAX: return MAX
        return val
