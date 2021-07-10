class Solution:
    # dp
    # f(i,j) is s1[:i+1],s2[:j+1] 是 interleaving s3[:i+j+1]
    # f(i,j) = f(i-1,j) or f(i,j-1)
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        if m + n != len(s3): return False
        dp = [[False] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            if s1[:i] == s3[:i]: dp[i][0] = True
        for j in range(1, m + 1):
            if s2[:j] == s3[:j]: dp[0][j] = True
        dp[0][0] = True
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s3[i + j - 1]: dp[i][j] = dp[i][j] or dp[i - 1][j]
                if s2[j - 1] == s3[i + j - 1]: dp[i][j] = dp[i][j] or dp[i][j - 1]
        return dp[n][m]