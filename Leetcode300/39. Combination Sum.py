class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(candidates, target, cur):
            if target < 0: return
            if target == 0:
                ans.append(cur)
                return

            for i in range(len(candidates)):
                dfs(candidates[i:], target - candidates[i], cur + [candidates[i]])

        dfs(candidates, target, [])
        return ans