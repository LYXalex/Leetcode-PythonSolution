class Solution:
    ## time complexity O(nlog(sum))
    def splitArray(self, nums, m: int) -> int:

        def checkValidMin(target):
            count = 1
            curSum = 0
            for num in nums:
                if curSum + num <= target:
                    curSum += num
                else:
                    count += 1
                    curSum = num
            return count

        left, right = max(nums), sum(nums)

        while left <= right:
            mid = left + (right - left) // 2
            print(mid, checkValidMin(mid))
            if checkValidMin(mid) <= m:
                right = mid - 1
            else:
                left = mid + 1
        return left

