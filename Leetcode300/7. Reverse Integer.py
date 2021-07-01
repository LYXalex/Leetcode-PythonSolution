class Solution:
    def reverse(self, x: int) -> int:
        MAX, MIN = 2 ** 31 - 1, -2 ** 31
        x = str(x)
        if x[0] != "-":
            x = x[::-1]
        else:
            x = "-" + x[1:][::-1]

        if MIN <= int(x) <= MAX:
            return int(x)
        else:
            return 0
