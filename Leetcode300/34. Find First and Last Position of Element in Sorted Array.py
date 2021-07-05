class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + r >> 1
            # find left boundary
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        if nums[l] == target:
            left = l
        else:
            return [-1, -1]

        # find right boundary
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + r + 1 >> 1
            if nums[mid] <= target:
                l = mid
            else:
                r = mid - 1
        return [left, l]