class Solution:
    #dp
    # f(i) 以i结尾的subarray的和(max)
    # f(i) f(i-1) < 0 f(i) = nums[i]
    #      f(i-1)>=0 f(i) = f(i-1)+nums[i]
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        # nums = [0]+nums
        dp = [0]*n
        dp[0] = nums[0]
        for i in range(1,n):
            dp[i] = nums[i]
            if dp[i-1] >=0: dp[i] += dp[i-1]
        return max(dp)