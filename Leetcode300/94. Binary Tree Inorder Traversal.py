# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # dfs
    def inorderTraversal1(self, root: TreeNode) -> List[int]:
        ans = []

        def dfs(cur):
            if not cur: return
            dfs(cur.left)
            ans.append(cur.val)
            dfs(cur.right)

        dfs(root)
        return ans

    # bfs
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        stack, ans = [], []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            ans.append(root.val)
            root = root.right
        return ans