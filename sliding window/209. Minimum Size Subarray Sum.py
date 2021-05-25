class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans, curSum, left = len(nums) + 1, 0, 0

        for i, num in enumerate(nums):
            curSum += num  # 进
            while curSum >= target:  # 出
                ans = min(ans, i - left + 1)  # 算
                curSum -= nums[left]
                left += 1
        return ans if ans != len(nums) + 1 else 0
