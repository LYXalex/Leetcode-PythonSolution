# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # recursive
    def zigzagLevelOrder1(self, root: TreeNode) -> List[List[int]]:

        ans = []

        def dfs(cur, level):
            if not cur: return
            if level > len(ans) - 1: ans.append([])
            if level % 2 == 0:
                ans[level].append(cur.val)
            else:
                ans[level].insert(0, cur.val)
            dfs(cur.left, level + 1)
            dfs(cur.right, level + 1)

        dfs(root, 0)
        return ans

    # iterative
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        ans, stack = [], [(root, 0)]
        while stack:
            cur, level = stack.pop()
            if level > len(ans) - 1: ans.append([])
            if level % 2 == 0:
                ans[level].append(cur.val)
            else:
                ans[level].insert(0, cur.val)
            if cur.right: stack.append((cur.right, level + 1))
            if cur.left: stack.append((cur.left, level + 1))
        return ans