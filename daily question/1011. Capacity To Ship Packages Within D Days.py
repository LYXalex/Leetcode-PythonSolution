import math


class Solution:
    # two pointers
    # time complexity: O(nlogk), where k = sum(weight)-max(weight)
    def shipWithinDays(self, weights, D: int) -> int:

        def finishShipped(maxW):
            curW = 0
            curD = 1
            for w in weights:

                if curW + w > maxW:
                    curD += 1
                    curW = w
                    if curD > D:
                        return False
                else:
                    curW += w
            return curD <= D

        left, right = max(weights), sum(weights) + 1

        while left < right:
            mid = left + (right - left) // 2
            if finishShipped(mid):
                right = mid
            else:
                left = mid + 1
        return left

