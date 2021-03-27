# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) :

        def dfs(cur,ans):
            if not cur:
                return

            ans.append(cur.val)
            dfs(cur.left,ans)
            dfs(cur.right,ans)

        ans = []
        dfs(root,ans)
        return ans

    def preorderTraversal(self, root: TreeNode) :

        ans = []
        if not root:
            return []
        stack = [root]

        while stack:
            curr = stack.pop()
            ans.append(curr.val)

            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return ans