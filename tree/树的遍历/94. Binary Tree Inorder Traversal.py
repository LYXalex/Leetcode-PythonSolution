# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:

    ## Recursion
    ## time complexity: O(n)
    ## space complexity: O(h) height for the recursion call
    def inorderTraversal1(self, root: TreeNode) :

        def dfs(cur,total):
            if not cur:
                return

            dfs(cur.left,total)
            total.append(cur.val)
            dfs(cur.right,total)

        total = []
        dfs(root,total)
        return total



    ## Interation
    ## time complexity: O(n)
    ## space complexity: O(n)

    def inorderTraversal2(self, root: TreeNode) :
        ans = []
        stack = []

        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            ans.append(curr.val)
            curr = curr.right
        return ans



