class Solution:
    # stack
    def longestValidParentheses1(self, s: str) -> int:
        i, cur, maxL, stack = 0, 0, 0, []
        while i < len(s):
            if s[i] == ")" and not stack:
                maxL = max(maxL, cur)
                cur = 0
            elif s[i] == ")" and stack:
                prev = stack.pop()
                cur = prev + cur + 2
                maxL = max(maxL, cur)
            elif s[i] == "(":
                stack.append(cur)
                cur = 0

            i += 1
        return maxL

    # 改进stack
    def longestValidParentheses1(self, s: str) -> int:
        stack, res, i = [-1], 0, 0
        while i < len(s):
            if s[i] == "(":
                stack.append(i)
            else:
                start = stack.pop()
                ## 遇到了两个)) 要terminate掉
                if not stack:
                    stack.append(i)
                # stack[-1]现在存的是可以组成valid的位置的前一个
                else:
                    res = max(res, i - stack[-1])
            i += 1
        return res

    # dp
    # f(i)代表的是i结尾最大的
    # if s[i] 是 ")" ① s[i-1]是"("  f[i-2]+2
    #                ② s[i-1]是“)”, f[i-1]+ f[i-dp[i-1]-2] + 2 当 s[i-dp[i-1]-1]是"("
    def longestValidParentheses(self, s: str) -> int:
        if len(s) < 2: return 0
        dp = [0] * (len(s) + 1)
        s = " " + s
        for i in range(2, len(s)):
            if s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2
                else:
                    if i - dp[i - 1] - 2 >= 0 and s[i - dp[i - 1] - 1] == "(":
                        dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
        return max(dp)





