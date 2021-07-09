class Solution:
    # two pass
    def sortColors1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroCount, oneCount, n = 0, 0, len(nums)
        for i, num in enumerate(nums):
            if num == 0: zeroCount += 1
            if num == 1: oneCount += 1

        for i in range(n):
            if i < zeroCount:
                nums[i] = 0
            elif i < zeroCount + oneCount:
                nums[i] = 1
            else:
                nums[i] = 2

    # one pass
    def sortColors(self, nums: List[int]) -> None:
        zeroPointer = 0
        twoPointer = len(nums) - 1
        i = 0
        while i <= twoPointer:
            if nums[i] == 0:
                nums[i], nums[zeroPointer] = nums[zeroPointer], nums[i]
                zeroPointer += 1
            elif nums[i] == 2:
                nums[i], nums[twoPointer] = nums[twoPointer], nums[i]
                twoPointer -= 1
                i -= 1
            i += 1