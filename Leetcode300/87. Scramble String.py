class Solution:
    def isScramble1(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True
        count1, count2 = Counter(s1), Counter(s2)
        if len(count1) != len(count2): return False
        for k, v in count1.items():
            if k not in count2: return False
            if count2[k] != v: return False

        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True
        return False

    # dp + memo
    def isScramble(self, s1, s2):

        memo = {}

        def helper(s1, s2):
            if (s1, s2) in memo: return memo[(s1, s2)]
            n, m = len(s1), len(s2)
            if n != m or sorted(s1) != sorted(s2):
                memo[(s1, s2)] = False
                return False
            if s1 == s2:
                memo[(s1, s2)] = True
                return True
            for i in range(1, n):
                if helper(s1[:i], s2[:i]) and helper(s1[i:], s2[i:]) or \
                        helper(s1[:i], s2[-i:]) and helper(s1[i:], s2[:-i]):
                    memo[(s1, s2)] = True
                    return True
            memo[(s1, s2)] = False
            return False

        return helper(s1, s2)