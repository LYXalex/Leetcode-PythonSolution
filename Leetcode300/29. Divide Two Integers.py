class Solution:
    O(32)

    def divide(self, dividend: int, divisor: int) -> int:
        MAX, MIN = 2 ** 31 - 1, -2 ** 31
        if dividend == MIN and divisor == -1: return MAX
        a, b, res = abs(dividend), abs(divisor), 0
        for i in range(31, -1, -1):
            if a >> i >= b:
                a -= b << i
                res += 1 << i
        if dividend > 0 and divisor > 0 or (dividend < 0 and divisor < 0):
            return res
        else:
            return -res
