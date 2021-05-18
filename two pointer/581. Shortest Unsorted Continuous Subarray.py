class Solution:
    def findUnsortedSubarray1(self, nums: List[int]) -> int:
        sortNums = sorted(nums)
        left = -1
        for i in range(len(nums)):
            if nums[i] != sortNums[i]:
                left = i
                break

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] != sortNums[i]:
                right = i
                break

        return (right - left + 1) if left != -1 else 0

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < len(nums) - 1 and nums[left] <= nums[left + 1]:
            left += 1
        if left == len(nums) - 1:
            return 0
        while right > 0 and nums[right] >= nums[right - 1]:
            right -= 1

        sub_min, sub_max = min(nums[left:right + 1]), max(nums[left:right + 1])
        while left > 0 and sub_min < nums[left - 1]:
            left -= 1
        while right < len(nums) - 1 and sub_max > nums[right + 1]:
            right += 1
        return right - left + 1





