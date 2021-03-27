
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children



class Solution:
    def postorder(self, root: 'Node'):# -> List[int]:

        def dfs(cur,ans):
            if not cur:
                return
            ans.insert(0,cur.val)
            for i in range(len(cur.children)-1,-1,-1):
                dfs(cur.children[i],ans)
        ans = []
        dfs(root,ans)
        return ans

    def postorder(self, root: 'Node'): # -> List[int]:

        if not root:
            return
        stack, ans = [root], []
        while stack:
            cur = stack.pop()
            ans.insert(0, cur.val)
            for child in cur.children:
                stack.append(child)

        return ans
