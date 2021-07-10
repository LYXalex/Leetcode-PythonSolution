# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # recursive (use global variable)
    import math
    def isValidBST1(self, root: TreeNode) -> bool:

        self.curV = -math.inf

        def dfs(cur):
            if not cur: return True
            l = dfs(cur.left)
            if cur.val > self.curV:
                self.curV = cur.val
            else:
                return False
            r = dfs(cur.right)

            return l and r

        return dfs(root)

    # recursive(do not use global variable)
    def isValidBST(self, root: TreeNode) -> bool:

        def dfs(cur, lowerBound, upperBound):
            if not cur: return True
            if cur.val >= upperBound or cur.val <= lowerBound:
                return False

            return dfs(cur.left, lowerBound, cur.val) and dfs(cur.right, cur.val, upperBound)

        return dfs(root, -math.inf, math.inf)

    # iterative