# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:

        map = {num: i for i, num in enumerate(post)}
        if not pre: return None

        def helper(pre, start, end):
            if not pre or start > end: return

            root = TreeNode(pre.pop(0))
            if not pre or start == end: return root
            index = map.get(pre[0])
            root.left = helper(pre, start, index)
            root.right = helper(pre, index + 1, end - 1)
            return root

        start, end = 0, len(pre) - 1
        return helper(pre, start, end)


