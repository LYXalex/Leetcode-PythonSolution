## time complexity: O(n)
## space complexity: O(n)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0

        def getDepth(node):
            if not node:
                return 0
            L = getDepth(node.left)
            R = getDepth(node.right)
            self.ans = max(self.ans, L + R)

            return max(L, R) + 1

        getDepth(root)
        return self.ans


