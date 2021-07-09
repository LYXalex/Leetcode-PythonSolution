class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + r >> 1
            if nums[mid] == target: return True
            if nums[mid] == nums[l]:
                l += 1
            elif nums[mid] > nums[l]:
                if target >= nums[l] and target < nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            else:
                if target <= nums[r] and target > nums[mid]:
                    l = mid
                else:
                    r = mid - 1

        return nums[l] == target




