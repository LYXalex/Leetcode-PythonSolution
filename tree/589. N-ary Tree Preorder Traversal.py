
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children



class Solution:
    def preorder(self, root: 'Node'): # -> List[int]:

        def dfs(cur,ans):
            if not cur:
                return
            ans.append(cur.val)
            for child in cur.children:
                dfs(child,ans)
        ans = []
        dfs(root,ans)
        return ans

    def preorder(self, root: 'Node'): # -> List[int]:

        while not root:
            return []
        stack, ans = [root], []
        while stack:
            cur = stack.pop(0)
            ans.append(cur.val)
            for i in range(len(cur.children) - 1, -1, -1):
                stack.insert(0, cur.children[i])
        return ans

