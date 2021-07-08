class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, 2 ** 31 - 1
        while r - l > 1e-8:
            mid = (l + r) / 2
            if mid * mid >= x:
                r = mid
            else:
                l = mid
        l = round(l)
        if l * l > x: return l - 1
        return l

