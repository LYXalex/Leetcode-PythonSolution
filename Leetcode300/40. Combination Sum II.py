class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        ans = []

        def dfs(index, target, cur):
            if target < 0: return
            if target == 0:
                if cur not in ans: ans.append(cur)
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]: continue
                if candidates[i] > target: break
                dfs(i + 1, target - candidates[i], cur + [candidates[i]])

        dfs(0, target, [])
        return ans

