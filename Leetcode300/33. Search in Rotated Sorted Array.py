class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + r >> 1
            # 有rotate
            if nums[mid] == target: return mid
            if nums[l] <= nums[mid]:
                if target < nums[mid] and target >= nums[l]:
                    r = mid
                else:
                    l = mid + 1
            else:
                if target > nums[mid] and target <= nums[r]:
                    l = mid
                else:
                    r = mid - 1
        if nums[l] == target: return l
        return -1
