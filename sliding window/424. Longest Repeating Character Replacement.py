class Solution:
    # O(26*n)
    import string
    def characterReplacement1(self, s: str, k: int) -> int:

        ans = 0
        for char in string.ascii_uppercase:
            left, curAction = 0, 0
            for i, each in enumerate(s):
                if each != char: curAction += 1  # 进
                while curAction > k:  # 出
                    if s[left] != char: curAction -= 1
                    left += 1
                ans = max(ans, i - left + 1)  # 算
        return ans

    # optimize
    # only need to get the current most character
    def characterReplacement(self, s: str, k: int) -> int:

        left, ans, map = 0, 0, [0] * 26

        for i, char in enumerate(s):
            map[ord(char) - ord('A')] += 1  # 进
            while i - left + 1 - max(map) > k:  # 出
                map[ord(s[left]) - ord('A')] -= 1
                left += 1
            ans = max(ans, i - left + 1)  # 算
        return ans