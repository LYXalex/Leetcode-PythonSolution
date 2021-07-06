class Solution:
    # dp
    # f(i,j) 代表 s[i:] 和 P[j:]匹配 (bool)
    def isMatch1(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[n][m] = True
        for i in range(n, -1, -1):
            for j in range(m - 1, -1, -1):
                # if i == n and j ==m: continue
                match = i < n and (s[i] == p[j] or p[j] == "?" or p[j] == "*")
                if p[j] == "*":
                    dp[i][j] = dp[i][j + 1] or (match and dp[i + 1][j])
                else:
                    dp[i][j] = match and dp[i + 1][j + 1]
        return dp[0][0]

    # dp + memo
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        memo = {}

        def dfs(i, j):
            if (i, j) not in memo:
                if j == m: return i == n
                match = i < n and j < m and (s[i] == p[j] or p[j] == "?" or p[j] == "*")
                if p[j] == "*":
                    ans = dfs(i, j + 1) or (match and dfs(i + 1, j))
                else:
                    ans = match and dfs(i + 1, j + 1)
                memo[(i, j)] = ans
                return memo[(i, j)]

        return dfs(0, 0)


