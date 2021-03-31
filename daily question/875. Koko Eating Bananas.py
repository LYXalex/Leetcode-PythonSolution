import math


class Solution:
    ## two pointers
    ## O(nlogk) where n is the # of piles and k is the piles contain maximum bananas
    def minEatingSpeed(self, piles, h: int) -> int:

        def finished(piles, rate):
            hours = 0
            for each in piles:
                hours += math.ceil(each / rate)
            return hours <= h

        left, right = math.ceil(sum(piles) / h), max(piles)
        # left,right = 1,max(piles)

        while left <= right:
            mid = left + (right - left) // 2

            if finished(piles, mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
