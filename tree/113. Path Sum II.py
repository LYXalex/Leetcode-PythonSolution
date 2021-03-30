# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int):# -> List[List[int]]:

        def dfs(cur, temp, ans):
            # print(temp)
            if not cur:
                return

            if not cur.left and not cur.right and sum(temp) + cur.val == targetSum:
                ans.append(temp + [cur.val])
                return

            temp.append(cur.val)
            dfs(cur.left, temp, ans)
            dfs(cur.right, temp, ans)
            del temp[-1]

        temp, ans = [], []
        dfs(root, temp, ans)
        return ans
