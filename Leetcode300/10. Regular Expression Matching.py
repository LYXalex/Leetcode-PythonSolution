class Solution:
    # recursion
    def isMatch1(self, s: str, p: str) -> bool:
        if not p: return not s
        match = False
        if s and (s[0] == p[0] or p[0] == '.'):
            match = True

        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (match and self.isMatch(s[1:], p))
        else:
            return match and self.isMatch(s[1:], p[1:])

    # dp
    # f(i,j) s[i:] and p[j:] match (bool)
    def isMatch1(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[-1][-1] = True
        for i in range(n, -1, -1):
            for j in range(m - 1, -1, -1):
                match = i < n and (s[i] == p[j] or p[j] == ".")
                if j + 1 < m and p[j + 1] == "*":
                    dp[i][j] = dp[i][j + 2] or (match and dp[i + 1][j])
                else:
                    dp[i][j] = match and dp[i + 1][j + 1]
        return dp[0][0]

    # recusion + memo
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        n, m = len(s), len(p)

        def dfs(i, j):
            if (i, j) not in memo:
                if j == m:
                    ans = (i == n)
                else:
                    match = i < n and (s[i] == p[j] or p[j] == ".")
                    if j + 1 < m and p[j + 1] == "*":
                        ans = dfs(i, j + 2) or (match and dfs(i + 1, j))
                    else:
                        ans = match and dfs(i + 1, j + 1)
                memo[(i, j)] = ans
            return memo[(i, j)]

        return dfs(0, 0)