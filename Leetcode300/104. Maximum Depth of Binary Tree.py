# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # recursive
    def maxDepth1(self, root: TreeNode) -> int:
        if not root:return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))

    # iterative
    # 记住要从左边pop
    def maxDepth(self, root: TreeNode) -> int:
        if not root:return 0
        stack,level = deque([root]),0
        while stack:
            length = len(stack)
            for i in range(length):
                cur = stack.popleft()
                if cur.left: stack.append(cur.left)
                if cur.right: stack.append(cur.right)
            level +=1
        return level