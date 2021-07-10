class Solution:
    # dp
    # f(i) 1-i 的BST排列 (sum)
    # G(t,n) 以t为顶 1-n的排列
    # f(i) = 求和(G(t,n)) where i =n, t 是1-n
    # G(t,n) = f(t-1)* f(n-t)
    # f(i) = 求和(f(t-1)*f(i-t)) where t 是1-i

    def numTrees(self, n: int) -> int:
        memo = {}

        def dfs(n):
            if n in memo: return memo[n]
            if n == 0:
                memo[0] = 1
                return memo[0]
            if n == 1:
                memo[1] = 1
                return memo[1]
            temp = 0
            for i in range(1, n + 1):
                temp += dfs(i - 1) * dfs(n - i)
            memo[n] = temp
            return memo[n]

        return dfs(n)


