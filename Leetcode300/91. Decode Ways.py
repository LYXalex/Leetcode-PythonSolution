class Solution:
    # dp
    # f(i) s[:i+1]有多少种表示 (sum)
    # f(i) f(i-1) + f(i-2)
    def numDecodings(self, s: str) -> int:
        n = len(s)
        s = " " + s
        dp = [0]*(n+1)
        dp[0] = 1
        for i in range(1,n+1):
            if int(s[i]) >= 1 and int(s[i]) <= 9: dp[i] += dp[i-1]
            if i >=2 and 10 <= int(s[i-1:i+1]) <= 26: dp[i] += dp[i-2]
        return dp[n]