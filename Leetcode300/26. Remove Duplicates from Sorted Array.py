class Solution:
    # two pointer
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[j - 1]:
                nums[j] = nums[i]
                j += 1
        return j

