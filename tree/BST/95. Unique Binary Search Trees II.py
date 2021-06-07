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
            if start > end: ans.append(None)
            for i in range(start, end + 1):
                for lchild in dfs(start, i - 1):
                    for rchild in dfs(i + 1, end):
                        root = TreeNode(i)
                        root.left = lchild
                        root.right = rchild
                        ans.append(root)
            return ans

        ans = []
        return dfs(1, n)
