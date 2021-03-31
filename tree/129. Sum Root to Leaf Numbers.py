# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:

        def dfs(cur, stringV):
            if not cur:
                return

            stringV += str(cur.val)
            if not cur.left and not cur.right:
                self.ans += int(stringV)

            dfs(cur.left, stringV)
            dfs(cur.right, stringV)

        stringV, self.ans = "", 0
        dfs(root, stringV)

        return self.ans

