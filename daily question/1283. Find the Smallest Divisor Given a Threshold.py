import math


class Solution:
    def smallestDivisor(self, nums, threshold: int) -> int:

        def checkDivisor(div):
            sum = 0
            for num in nums:
                sum += math.ceil(num / div)
                if sum > threshold:
                    break
            return sum <= threshold

        left, right = 1, max(nums) + 1

        while left < right:
            mid = left + (right - left) // 2
            if checkDivisor(mid):
                right = mid
            else:
                left = mid + 1
        return left