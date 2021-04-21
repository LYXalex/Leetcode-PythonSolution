class Solution:
    ## divide and conquer time log(n)
    def findMin1(self, nums) -> int:
        def helper(low, high):
            if low + 1 >= high:
                return min(nums[low], nums[high])
            ## add
            if nums[low] < nums[high]: return nums[low]
            mid = low + (high - low) // 2

            return min(helper(low, mid), helper(mid + 1, high))

        return helper(0, len(nums) - 1)

    # binary search   time log(n)
    def findMin(self, nums) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]
