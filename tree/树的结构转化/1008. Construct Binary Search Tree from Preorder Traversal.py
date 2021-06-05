# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    import math
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def helper(preorder, bound):
            if not preorder or preorder[0] > bound: return None
            cur = preorder.pop(0)
            root = TreeNode(cur)
            root.left = helper(preorder, cur)
            root.right = helper(preorder, bound)
            return root

        bound = math.inf
        return helper(preorder, bound)
