# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    import math
    def goodNodes(self, root: TreeNode) -> int:

        self.ans = 0

        def dfs(node, preMax):
            if not node: return
            if node.val >= preMax: self.ans += 1
            preMax = max(preMax, node.val)
            dfs(node.left, preMax)
            dfs(node.right, preMax)

        preMax = -math.inf
        dfs(root, preMax)
        return self.ans