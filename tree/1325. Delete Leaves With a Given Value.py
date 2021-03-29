# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def removeLeafNodes1(self, root: TreeNode, target: int) -> TreeNode:

        self.change = True

        def dfs(cur):
            if not cur:
                return None
            if (not cur.left and not cur.right) and cur.val == target:
                self.change = True
                return None
            elif (not cur.left and not cur.right) and cur.val != target:
                return cur
            else:
                cur.left = dfs(cur.left)
                cur.right = dfs(cur.right)
                return cur

        temp = root
        while self.change and temp:
            self.change = False
            temp = dfs(temp)

        return temp

    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:

        if not root:
            return None

        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        if (not root.left and not root.right) and root.val == target:
            return None

        return root


