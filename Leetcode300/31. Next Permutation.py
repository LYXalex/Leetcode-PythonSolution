class Solution:
    def nextPermutation1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        finish = False
        if n == 1: return nums
        for i in range(n-2,-1,-1):
            cur = nums[i]
            if finish: break
            for j in range(n-1,i,-1):
                if cur < nums[j]:
                    nums[i],nums[j] = nums[j],cur
                    temp = nums[i+1:]
                    temp.sort()
                    nums[i+1:] = temp
                    finish = True
                    break
        if not finish: return nums.sort()
        return nums

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        finish = False
        if n == 1: return nums
        finish = False
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                start = i+1
                while start < n and nums[start] > nums[i]: start+=1
                nums[i],nums[start-1] = nums[start-1],nums[i]
                temp = nums[i+1:]
                temp.sort()
                nums[i+1:] = temp
                finish = True
                break
        if not finish: return nums.sort()
        return nums