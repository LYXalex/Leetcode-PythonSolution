class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        ans = ""
        if not path: return "/"
        stack = []
        while path:
            cur = path.pop(0)
            if not cur or cur == ".":
                continue
            elif cur == ".." and stack:
                stack.pop()
            elif cur == ".." and not stack:
                continue
            else:
                stack.append(cur)
        if not stack:
            return "/"
        else:
            return "/" + "/".join(stack)
