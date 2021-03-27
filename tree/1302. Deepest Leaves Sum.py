# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:

        def dfs(cur, level, sum):
            if not cur:
                return
            if level > len(sum) - 1:
                sum.append([])
                sum[level] = cur.val
            else:
                sum[level] += cur.val
            if cur.left:
                dfs(cur.left, level + 1, sum)
            if cur.right:
                dfs(cur.right, level + 1, sum)

        sum = []
        dfs(root, 0, sum)
        return sum[-1]
