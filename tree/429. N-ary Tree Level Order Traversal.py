
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children



class Solution:
    def levelOrder(self, root: 'Node'): #-> List[List[int]]

        ans = []
        def dfs(cur,level,ans):
            if not cur:
                return

            if level > len(ans)-1:
                ans.append([])
            ans[level].append(cur.val)

            for child in cur.children:
                dfs(child,level+1,ans)

        dfs(root,0,ans)
        return ans

    def levelOrder(self, root: 'Node'): # -> List[List[int]]
        while not root:
            return []
        ans, stack = [], [(root, 0)]

        while stack:
            cur, level = stack.pop()
            if level > len(ans) - 1:
                ans.append([])
            ans[level].append(cur.val)
            for child in cur.children:
                stack.insert(0, (child, level + 1))
        return ans








