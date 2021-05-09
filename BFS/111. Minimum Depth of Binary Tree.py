# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ## dfs
    def minDepth1(self, root: TreeNode) -> int:

        if not root:
            return 0

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        if not root.left: return right + 1
        if not root.right: return left + 1

        return min(left, right) + 1

    def minDepth(self, root) -> int:
        if not root:
            return 0
        queue = deque([(root, 1)])
        while queue:
            cur, step = queue.popleft()
            if not cur.left and not cur.right:
                return step

            if cur.left:
                queue.append((cur.left, step + 1))
            if cur.right:
                queue.append((cur.right, step + 1))
        return step

