class Solution:
    # divide and conquer
    def findMin1(self, nums) -> int:
        def helper(l, r):
            if l + 1 >= r:
                return min(nums[l], nums[r])
            mid = l + (r - l) // 2

            if nums[l] < nums[r]:
                return nums[l]
            return min(helper(l, mid), helper(mid + 1, r))

        return helper(0, len(nums) - 1)

    # binary search
    def findMin(self, nums) -> int:
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[r]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid
            else:
                r -= 1

        return min(nums[r], nums[l])
