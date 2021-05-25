class Solution:
    def longestSubstring1(self, s: str, k: int) -> int:
        count = Counter(s)
        start, maxS = 0, 0

        for i, char in enumerate(s):
            if count[char] < k:
                maxS = max(maxS, self.longestSubstring(s[start:i], k))
                start = i + 1
        return len(s) if start == 0 else max(maxS, self.longestSubstring(s[start:], k))

    # sliding window  O(26*n)
    def longestSubstring(self, s: str, k: int) -> int:
        count = Counter(s)
        maxUnique = len(count)
        ans = [0] * maxUnique
        for unique in range(1, maxUnique + 1):
            map, validCount, left = {}, 0, 0
            for i, char in enumerate(s):
                map[char] = map.get(char, 0) + 1
                if map[char] == k: validCount += 1  # 进

                while len(map) > unique:  # 出
                    if map[s[left]] == k: validCount -= 1
                    map[s[left]] -= 1
                    if map[s[left]] == 0: del map[s[left]]
                    left += 1

                if validCount == unique and validCount == len(map):
                    ans[unique - 1] = max(ans[unique - 1], i - left + 1)  # 算

        return max(ans)








