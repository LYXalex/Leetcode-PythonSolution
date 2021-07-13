# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        def dfs(start,end):
            if start > end:return None
            mid = start + end >> 1
            root  = TreeNode(nums[mid])
            root.left = dfs(start,mid-1)
            root.right = dfs(mid+1,end)
            return root
        return dfs(0,len(nums)-1)