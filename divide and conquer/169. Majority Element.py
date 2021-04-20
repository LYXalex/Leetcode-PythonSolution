import collections


class Solution:
    # hashmap   time: O(n) space: O(n)
    def majorityElement(self, nums) -> int:
        appearedDict = collections.defaultdict(int)
        for num in nums:
            appearedDict[num] += 1
            if appearedDict[num] > len(nums) // 2:
                return num
        return -1

    # divide and conquer  time:O(nlog(n)) space:O(log(n))
    def majorityElement2(self, nums) -> int:

        def helper(low, high):
            if low == high:
                return nums[low]
            mid = low + (high - low) // 2
            l = helper(low, mid)
            r = helper(mid + 1, high)

            if l == r:
                return l
            lc = sum(1 for i in range(low, high + 1) if nums[i] == l)
            rc = sum(1 for i in range(low, high + 1) if nums[i] == r)

            return l if lc > rc else r

        return helper(0, len(nums) - 1)

    # moore time: O(n) space: O(1)
    def majorityElement(self, nums) -> int:
        if not nums:
            return
        target = nums[0]
        curN = 1
        for i in range(1, len(nums)):
            if curN == 0:
                target = nums[i]
                curN = 1
            else:
                if nums[i] != target:
                    curN -= 1
                else:
                    curN += 1
        return target
