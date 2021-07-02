class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, n = [], len(nums)
        if n < 3: return res
        nums.sort()
        for i in range(n - 2):
            if i - 1 >= 0 and nums[i] == nums[i - 1]: continue
            p1, p2, target = i + 1, n - 1, -nums[i]
            while p1 < p2:
                val = nums[p1] + nums[p2]
                if val > target:
                    p2 -= 1
                elif val < target:
                    p1 += 1
                else:
                    res.append([nums[i], nums[p1], nums[p2]])
                    p1 += 1
                    p2 -= 1
                    while p1 < n and nums[p1] == nums[p1 - 1]: p1 += 1
                    while p2 >= 0 and nums[p2] == nums[p2 + 1]: p2 -= 1

        return res

