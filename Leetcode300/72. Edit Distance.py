class Solution:
    #dp
    #f(i,j): s1[:i]-> s2[:j]的操作(min)
    #f(i,j): 最后一步是这三种的任意一种，求min
    #insert: f(i,j-1)+1
    #delete: f(i-1,j)+1
    #replace: f(i-1,j-1)+1
    def minDistance(self, word1: str, word2: str) -> int:
        n,m = len(word1),len(word2)
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(1,n+1): dp[i][0] = i
        for j in range(1,m+1): dp[0][j] = j
        word1,word2 = " "+word1," "+word2
        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[i] == word2[j]:
                    dp[i][j] = min(dp[i][j-1]+1,dp[i-1][j]+1,dp[i-1][j-1])
                else:
                    dp[i][j] = min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1
        return dp[n][m]