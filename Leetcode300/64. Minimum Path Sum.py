import math
class Solution:
    # dp O(n^2) O(n^2)
    # f(i,j) 到i,j的path 路径的sum(min)
    # f(i,j) 上一步是在上一个格子 f(i-1,j)
    #          上一步是在左边的格子 f(i,j-1)
    def minPathSum(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = math.inf
        for j in range(m+1):
            dp[0][j] = math.inf
        dp[1][1] = grid[0][0]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if i !=1 or j!=1:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i-1][j-1]
        return dp[n][m]