# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n)
    def countNodes1(self, root: TreeNode) -> int:

        if not root:
            return 0
        l = self.countNodes(root.left)
        r = self.countNodes(root.right)

        return l + r + 1

    # since left hegiht always >= right hegiht
    ## time complexity: O(log(n)*log(n))
    def countNodes(self, root: TreeNode) -> int:

        def getDepth(node):
            if not node:
                return 0
            return 1 + getDepth(node.left)

        if not root:
            return 0

        l = getDepth(root.left)
        r = getDepth(root.right)

        if l == r:
            return 2 ** l + self.countNodes(root.right)
        else:
            return 2 ** r + self.countNodes(root.left)
