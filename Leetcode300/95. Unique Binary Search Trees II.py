# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## since we need to return the exact answer instead the number we cannot use dp
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        def dfs(start, end):
            ans = []
            if end < start: ans.append(None)

            for i in range(start, end + 1):
                lchild = dfs(start, i - 1)
                rchild = dfs(i + 1, end)
                for l in lchild:
                    for r in rchild:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        ans.append(root)
            return ans

        return dfs(1, n)
