class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        nums.sort()

        def dfs(cur, nums):
            if cur not in self.ans:
                self.ans.append(cur)
            for i, num in enumerate(nums):
                dfs(cur + [num], nums[i + 1:])

        dfs([], nums)
        return self.ans


