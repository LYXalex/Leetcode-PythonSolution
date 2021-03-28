class Solution:
    def maximumScore(self, nums, k: int) -> int:
        start = end = k
        maxAns, curMin = 0, nums[k]

        while start >= 0 or end < len(nums):
            while start >= 0 and nums[start] >= curMin:
                start -= 1
            while end < len(nums) and nums[end] >= curMin:
                end += 1
            maxAns = max(maxAns, curMin * (end - start - 1))

            if start <= 0 and end >= len(nums) - 1:
                break
            elif start == -1:
                curMin = nums[end]
            elif end == len(nums):
                curMin = nums[start]
            else:
                curMin = max(nums[end], nums[start])

        return maxAns





