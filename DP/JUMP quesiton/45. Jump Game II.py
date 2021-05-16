class Solution:
    import math
    ## dp O(n^2)
    def jump1(self, nums: List[int]) -> int:

        dp = [math.inf] * len(nums)
        dp[0] = 0
        for i in range(len(nums) - 1):
            step = min(i + nums[i], len(nums) - 1)
            for j in range(i + 1, step + 1):
                dp[j] = min(dp[j], dp[i] + 1)
        return dp[-1]

    ## greedy  O(n)
    def jump(self, nums: List[int]) -> int:

        ans, last_index, cur_cover = 0, 0, 0
        if len(nums) == 1:
            return 0
        for i, num in enumerate(nums):

            ## keep track the current largest coverage
            cur_cover = max(cur_cover, i + num)

            ## when reach to the last step max index, we need to update
            if i == last_index:
                ans += 1
                last_index = cur_cover
                if cur_cover >= len(nums) - 1:
                    return ans
        return ans
