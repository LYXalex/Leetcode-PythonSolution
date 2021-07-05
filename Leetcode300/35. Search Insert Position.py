class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + r >> 1
            if nums[mid] == target: return mid
            if nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        if nums[l] >= target:
            return l
        else:
            return l + 1
