class Solution:
    # 2 2
    # 3 3
    # 4 5
    def climbStairs1(self, n: int) -> int:
        memo = {}

        def helper(n):
            if n in memo: return memo[n]
            if n == 1:
                memo[1] = 1
            elif n == 2:
                memo[2] = 2
            else:
                memo[n] = helper(n - 1) + helper(n - 2)
            return memo[n]

        return helper(n)

    # dp
    # f(i) = 到i的路径(sum)
    # f(i) = f(i-1) + f(i-2)
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]