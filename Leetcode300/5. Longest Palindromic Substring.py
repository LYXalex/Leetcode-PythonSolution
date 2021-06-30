class Solution:
    # f(i,j) represent index i to j is palindrome or not
    # f(i,j) = s[i] == s[j] and f(i+1,j-1)
    # O(n^2)
    def longestPalindrome(self, s: str) -> str:
        maxL, n, maxI, maxJ = 0, len(s), -1, -1
        dp = [[False] * n for _ in range(n)]

        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if j - i == 1 or j - i == 0 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        if j - i + 1 > maxL:
                            maxL = j - i + 1
                            maxI = i
                            maxJ = j
        return s[maxI:maxJ + 1]