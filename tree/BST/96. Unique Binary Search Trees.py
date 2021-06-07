class Solution:
    # dp
    # G(n) = sigma(1 ~ n) F(i,n) where i is the root number
    # F(i,n) = G(i-1)*G(n-i)
    # G(n) = sigma(1~n) G(i-1)*G(n-i)
    # base case G(0) =1  G(1) = 1
    # G(2) = G(0)G(1) + G(1)G(0) = 2
    # G(3) = G(2)G(0) + G(1)G(1) + G(0)G(2) = 5

    def numTrees1(self, n: int) -> int:

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[-1]

    # recusrion + memo
    def numTrees(self, n: int) -> int:

        def dfs(num, memo):
            if num == 0 or num == 1: return 1
            if num in memo: return memo[num]

            sum = 0
            for i in range(1, num + 1):
                sum += dfs(i - 1, memo) * dfs(num - i, memo)
            memo[num] = sum
            return memo[num]

        memo = {}
        return dfs(n, memo)

