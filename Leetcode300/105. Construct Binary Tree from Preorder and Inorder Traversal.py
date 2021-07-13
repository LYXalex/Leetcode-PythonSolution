# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        ans = []
        map = {num: i for i, num in enumerate(inorder)}  # 可以用dictionary优化

        def helper(preorder, start, end):
            if not preorder or (start > end): return None
            cur = preorder.pop(0)
            i = map.get(cur)
            root = TreeNode(cur)
            root.left = helper(preorder, start, i - 1)
            root.right = helper(preorder, i + 1, end)

            return root

        return helper(preorder, 0, len(inorder) - 1)