# ## BFS
# ## time complexity O(n) number of nodes
# ## space complexity O(n)


class Solution:
    # iterative
    def levelOrder1(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        stack, ans = [(root, 0)], []
        while stack:
            cur, level = stack.pop(0)
            if level > len(ans) - 1:
                ans.append([])
            ans[level].append(cur.val)
            if cur.left:
                stack.append((cur.left, level + 1))
            if cur.right:
                stack.append((cur.right, level + 1))
        return ans

    # recursion
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        def dfs(cur, ans, level):
            if not cur:
                return
            if level > len(ans) - 1: ans.append([])
            ans[level].append(cur.val)
            if cur.left:
                dfs(cur.left, ans, level + 1)
            if cur.right:
                dfs(cur.right, ans, level + 1)

        ans, level = [], 0
        dfs(root, ans, level)
        return ans




