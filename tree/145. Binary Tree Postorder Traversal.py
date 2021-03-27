# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) :

        def dfs(cur,ans):
            if not cur:
                return
            dfs(cur.left,ans)
            dfs(cur.right,ans)
            ans.append(cur.val)

        ans = []
        dfs(root,ans)
        return ans

    def postorderTraversal(self, root: TreeNode) :

        if not root:
            return []
        ans, stack = [], [root]
        while stack:
            cur = stack.pop()
            ans.insert(0, cur.val)

            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)

        return ans
