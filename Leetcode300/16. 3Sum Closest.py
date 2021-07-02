import math


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        n, res, diff = len(nums), 0, math.inf
        for i in range(n - 2):
            l, r, need = i + 1, n - 1, target - nums[i]
            while l < r:
                val = nums[l] + nums[r]
                if val > need:
                    r -= 1
                elif val < need:
                    l += 1
                else:
                    return target
                if abs(val + nums[i] - target) < diff:
                    diff = abs(val + nums[i] - target)
                    res = val + nums[i]
        return res

