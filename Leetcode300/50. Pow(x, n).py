class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 or x == 1:
            return x

        def helper(x, n):
            if n == 0: return 1
            y = helper(x, n // 2)
            if n % 2 == 0:
                return y * y
            else:
                return y * y * x

        if n >= 0:
            return helper(x, n)
        else:
            return 1 / (helper(x, -n))

