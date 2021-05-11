class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n, self.ans = len(nums), []
        nums.sort()

        def dfs(cur, nums):
            if len(cur) == n and cur not in self.ans:
                self.ans.append(cur)
            for i, num in enumerate(nums):
                if i > 0 and num == nums[i - 1]:
                    continue
                dfs(cur + [num], nums[:i] + nums[i + 1:])

        dfs([], nums)
        return self.ans
