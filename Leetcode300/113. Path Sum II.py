# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        ans = []
        if not root: return ans

        def dfs(cur, target, temp):
            if not cur: return
            if not cur.left and not cur.right and target == cur.val:
                ans.append(temp + [cur.val])
                return
            dfs(cur.left, target - cur.val, temp + [cur.val])
            dfs(cur.right, target - cur.val, temp + [cur.val])

        dfs(root, targetSum, [])
        return ans
