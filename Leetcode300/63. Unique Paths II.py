class Solution:
    # dp O(n^2) O(n^2)
    # f(i,j) 到i,j的unique path(sum)
    # f(i,j) 上一步是在上一个格子 f(i-1,j)
    #          上一步是在左边的格子 f(i,j-1)
    def uniquePathsWithObstacles1(self, obstacleGrid: List[List[int]]) -> int:
        n,m = len(obstacleGrid),len(obstacleGrid[0])
        dp = [[0]*(m+1) for _ in range(n+1)]
        dp[1][1] = 1 if not obstacleGrid[0][0] else 0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if (i !=1 or j != 1) and not obstacleGrid[i-1][j-1]:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[n][m]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n,m = len(obstacleGrid),len(obstacleGrid[0])
        dp = [0]*(m+1)
        dp[1] = 1 if not obstacleGrid[0][0] else 0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if (i !=1 or j != 1) and not obstacleGrid[i-1][j-1]:
                    dp[j] = dp[j] + dp[j-1]
                elif obstacleGrid[i-1][j-1]:dp[j] = 0
        return dp[m]