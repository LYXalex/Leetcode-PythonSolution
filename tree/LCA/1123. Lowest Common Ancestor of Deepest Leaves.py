# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves1(self, root: TreeNode) -> TreeNode:

        def getDepth(root):
            if not root: return 0
            return 1 + max(getDepth(root.left), getDepth(root.right))

        length = getDepth(root)

        def findDeepestNodes(root, ans, level):
            if not root: return
            if level == length: ans.add(root)
            findDeepestNodes(root.left, ans, level + 1)
            findDeepestNodes(root.right, ans, level + 1)

        ans, level = set(), 1
        findDeepestNodes(root, ans, level)

        def helper(root):
            if not root: return
            if root in ans: return root
            left = helper(root.left)
            right = helper(root.right)
            if left and right: return root
            if left: return left
            if right: return right
            return None

        return helper(root)

    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:

        def helper(root, d):
            if not root: return (None, d)
            left, curL = helper(root.left, d + 1)
            right, curR = helper(root.right, d + 1)

            if curL == curR: return root, curL
            if curL > curR: return left, curL
            if curR > curL: return right, curR

        ans, height = helper(root, 0)
        print(height)
        return ans

