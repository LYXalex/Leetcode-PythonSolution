class Solution:
    # dfs
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = []

        def dfs(nums, cur):
            ans.append(cur[:])
            if not nums: return
            for i in range(len(nums)):
                cur.append(nums[i])
                dfs(nums[i + 1:], cur)
                cur.pop()

        dfs(nums, [])
        return ans