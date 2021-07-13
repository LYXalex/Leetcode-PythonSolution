# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        map = {num: i for i, num in enumerate(inorder)}

        def helper(start, end, postorder):
            if not postorder or (start > end): return None
            cur = postorder.pop()
            i = map.get(cur)

            root = TreeNode(cur)
            root.right = helper(i + 1, end, postorder)
            root.left = helper(start, i - 1, postorder)

            return root

        return helper(0, len(inorder) - 1, postorder)
