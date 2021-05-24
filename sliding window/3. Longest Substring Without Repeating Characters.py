class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        left, ans = 0, 0
        count = {}
        for i, char in enumerate(s):
            if char in count:
                left = max(left, count[char] + 1)
            count[char] = i
            ans = max(ans, i - left + 1)
        return ans


