## time complexity:O(n)
## space complexity: O(n) level of recursive stack
# Definition for a binary tree node.
import math
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum1(self, root: TreeNode) -> int:

        self.ans = -math.inf

        def getSum(node):
            if not node:
                return 0
            L = getSum(node.left)
            R = getSum(node.right)

            maxV = max(0, R) + max(0, L) + node.val
            self.ans = max(self.ans, maxV)
            return max(L, R, 0) + node.val

        getSum(root)
        return self.ans

    def maxPathSum(self, root: TreeNode) -> int:

        self.sum = -math.inf

        def helper(node):
            if not node:
                return 0

            left = helper(node.left)
            right = helper(node.right)

            left = left if left > 0 else 0
            right = right if right > 0 else 0
            maxV = node.val + left + right
            self.sum = max(maxV, self.sum)

            return max(left, right) + node.val

        helper(root)

        return self.sum




