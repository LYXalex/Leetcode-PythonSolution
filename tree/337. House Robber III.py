# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:

        mem = {}

        def dfs(node):
            if not node:
                return 0
            if node in mem:
                return mem[node]
            ll = dfs(node.left.left) if node.left else 0
            lr = dfs(node.left.right) if node.left else 0
            rl = dfs(node.right.left) if node.right else 0
            rr = dfs(node.right.right) if node.right else 0

            mem[node] = max(node.val + ll + lr + rl + rr, dfs(node.left) + dfs(node.right))
            return mem[node]

        return dfs(root)
