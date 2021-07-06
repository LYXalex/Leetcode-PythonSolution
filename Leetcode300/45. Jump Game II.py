import math


class Solution:
    # O(n^2)
    def jump1(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [math.inf] * n
        dp[0] = 0
        for i in range(0, n):
            for j in range(i + 1, min(i + nums[i] + 1, n)):
                dp[j] = min(dp[j], dp[i] + 1)
        return dp[n - 1]

    # greedy
    def jump(self, nums: List[int]) -> int:
        step, cur_cover, last_index = 0, 0, 0
        if len(nums) == 1: return 0
        for i in range(len(nums)):
            cur_cover = max(cur_cover, i + nums[i])
            if i == last_index:
                step += 1
                last_index = cur_cover
                if last_index >= len(nums) - 1:
                    return step


