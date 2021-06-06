# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        map = {num: i for i, num in enumerate(inorder)}

        def helper(postorder, start, end):
            if not postorder or start > end: return
            cur = postorder.pop()
            root = TreeNode(cur)
            index = map[cur]
            root.right = helper(postorder, index + 1, end)
            root.left = helper(postorder, start, index - 1)
            return root

        start, end = 0, len(inorder) - 1
        return helper(postorder, start, end)
