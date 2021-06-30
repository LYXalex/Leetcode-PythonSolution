class Solution:
    # basic two pointer
    def lengthOfLongestSubstring1(self, s: str) -> int:

        cnt, j, res = {}, 0, 0
        for i in range(len(s)):
            cnt[s[i]] = cnt.get(s[i], 0) + 1
            while cnt[s[i]] > 1:
                cnt[s[j]] -= 1
                j += 1
            res = max(res, i - j + 1)
        return res

    # using hashMap to store the last appear location
    def lengthOfLongestSubstring(self, s: str) -> int:

        lastAppear, res, start = {}, 0, 0
        for i in range(len(s)):
            if s[i] in lastAppear:
                start = max(start, lastAppear[s[i]] + 1)
            lastAppear[s[i]] = i
            res = max(res, i - start + 1)
        return res

