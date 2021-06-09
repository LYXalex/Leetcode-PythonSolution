# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # pure recursion 算当前的最大值
    def longestZigZag1(self, root: TreeNode) -> int:

        self.ans = 0

        # curD = 0 represent left else right
        def helper(node, isLeft):
            if not node: return 0
            left = helper(node.left, False)
            right = helper(node.right, True)

            self.ans = max(self.ans, max(left, right))

            return 1 + left if isLeft else 1 + right

        helper(root, True)
        helper(root, False)
        return self.ans

    # 每个子树的leftSum,rightSum 都得到
    def longestZigZag(self, root: TreeNode) -> int:

        def helper(node):
            if not node: return 0, 0
            leftV = helper(node.left)
            rightV = helper(node.right)
            rightSum = rightV[0] + 1
            leftSum = leftV[1] + 1
            self.ans = max(self.ans, max(leftSum, rightSum))

            return leftSum, rightSum

        self.ans = 0
        helper(root)
        return self.ans - 1






