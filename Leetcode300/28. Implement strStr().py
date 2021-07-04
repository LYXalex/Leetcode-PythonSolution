class Solution:
    # O(mn) 暴力
    def strStr1(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        if not haystack: return -1
        needle = needle[::-1]
        for i in range(len(haystack)):
            if i + 1 < len(needle): continue
            j, k = i, 0
            while j >= 0 and k < len(needle) and haystack[j] == needle[k]:
                j -= 1
                k += 1
            if k == len(needle): return i - len(needle) + 1
        return -1

    # O(n) kmp
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        n, m = len(haystack), len(needle)
        haystack = " " + haystack
        needle = " " + needle
        ne = [0] * (m + 1)
        j = 0
        for i in range(2, m + 1):
            while j and needle[i] != needle[j + 1]: j = ne[j]
            if needle[i] == needle[j + 1]: j += 1
            ne[i] = j

        j = 0
        for i in range(1, n + 1):
            while j and haystack[i] != needle[j + 1]: j = ne[j]
            if needle[j + 1] == haystack[i]: j += 1
            if j == m:
                return i - m
        return -1

