class Solution:

    ## time complexity O(n^2) dp top-down
    def canJump1(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        if not nums:
            return False
        dp[0] = True
        maxI = 0
        for i, each in enumerate(dp):
            if each:
                index = i + nums[i]
                if index >= n - 1:
                    return True
                if i > maxI:
                    return False
                if index <= maxI:
                    continue
                else:
                    maxI = index
                    for j in range(i + 1, i + nums[i] + 1):
                        dp[j] = True
        return False

    ## greedy
    def canJump2(self, nums: List[int]) -> bool:
        lastIndex = len(nums) - 1

        if len(nums) < 1:
            return True
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= lastIndex:
                lastIndex = i

        return lastIndex == 0



