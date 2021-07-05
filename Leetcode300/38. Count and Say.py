class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"

        s = self.countAndSay(n - 1)
        num, val, ans = 1, s[0], ""
        for i in range(1, len(s)):
            if s[i] == val:
                num += 1
            else:
                ans += str(num) + str(val)
                num = 1
                val = s[i]
        ans += str(num) + str(val)
        return ans
