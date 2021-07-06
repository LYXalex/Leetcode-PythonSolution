class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(nums, cur):
            if not nums:
                ans.append(cur)
                return
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i + 1:], cur + [nums[i]])

        dfs(nums, [])
        return ans


