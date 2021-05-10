class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n, self.ans = len(nums), []

        def dfs(cur, nums):
            if len(cur) == n:
                self.ans.append(cur)

            for i, num in enumerate(nums):
                dfs(cur + [num], nums[:i] + nums[i + 1:])

        dfs([], nums)
        return self.ans
