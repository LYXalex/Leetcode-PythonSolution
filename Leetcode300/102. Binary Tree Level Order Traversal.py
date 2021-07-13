# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # recursive
    def levelOrder1(self, root: TreeNode) -> List[List[int]]:

        ans = []

        def dfs(cur, level):
            if not cur: return

            if level > len(ans) - 1: ans.append([])
            ans[level].append(cur.val)
            dfs(cur.left, level + 1)
            dfs(cur.right, level + 1)

        dfs(root, 0)
        return ans

    # iterative
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root: return ans
        stack = [(root, 0)]
        while stack:
            root, level = stack.pop()
            if level > len(ans) - 1: ans.append([])
            ans[level].append(root.val)
            if root.right: stack.append((root.right, level + 1))
            if root.left: stack.append((root.left, level + 1))
        return ans