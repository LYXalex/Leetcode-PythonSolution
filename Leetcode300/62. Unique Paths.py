import math


class Solution:
    # dp O(n^2) O(n^2)
    # f(i,j) 到i,j的unique path(sum)
    # f(i,j) 上一步是在上一个格子 f(i-1,j)
    #          上一步是在左边的格子 f(i,j-1)
    def uniquePaths1(self, m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[1][1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i != 1 or j != 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m][n]

    # dp 滚动数组 优化空间 O(n^2)  O(n)
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i != 1 or j != 1:
                    dp[j] = dp[j] + dp[j - 1]
        return dp[n]

    # math 一共在m-n-2步里面找 m-1步向下
    def uniquePaths(self, m: int, n: int) -> int:
        if not m or not n:
            return 0
        return int(math.factorial(m + n - 2) / (math.factorial(n - 1) * math.factorial(m - 1)))

