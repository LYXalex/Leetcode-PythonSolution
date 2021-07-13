# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # recursive
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:

        def tHeight(root):
            if not root: return 0
            return 1 + max(tHeight(root.left), tHeight(root.right))

        t = tHeight(root)
        ans = []
        for i in range(t): ans.append([])

        def dfs(cur, level):
            if not cur: return
            ans[t - 1 - level].append(cur.val)
            dfs(cur.left, level + 1)
            dfs(cur.right, level + 1)

        dfs(root, 0)
        return ans
