# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import math
class Solution:
    def verticalTraversal(self, root: TreeNode): # -> List[List[int]]:

        def dfs(cur, col, row, temp):
            if not cur:
                return
            temp.append((cur.val, col, row))
            if cur.left:
                dfs(cur.left, col - 1, row + 1, temp)
            if cur.right:
                dfs(cur.right, col + 1, row + 1, temp)

        temp = []
        dfs(root, 0, 0, temp)
        temp.sort(key=lambda x: (x[1], x[2], x[0]))
        ans = []
        cur = -math.inf
        for val, col, row in temp:
            if cur < col:
                cur = col
                ans.append([])
            ans[-1].append(val)
        return ans