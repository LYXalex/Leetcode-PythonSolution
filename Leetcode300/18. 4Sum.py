class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n, res = len(nums), []
        if n < 4: return res
        nums.sort()
        for i in range(n - 3):
            if i == 0 or nums[i] != nums[i - 1]:
                for j in range(i + 1, n - 2):
                    if j == i + 1 or nums[j] != nums[j - 1]:
                        l, r, need = j + 1, n - 1, target - nums[i] - nums[j]
                        while l < r:
                            val = nums[l] + nums[r]
                            if val > need:
                                r -= 1
                            elif val < need:
                                l += 1
                            else:
                                res.append([nums[i], nums[j], nums[l], nums[r]])
                                l += 1
                                r -= 1
                                while l < n and nums[l] == nums[l - 1]: l += 1
                                while r >= 0 and nums[r] == nums[r + 1]: r -= 1
        return res

