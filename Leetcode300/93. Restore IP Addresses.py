class Solution:
    # dfs
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []

        def dfs(s, cur):
            if len(cur) == 4 and not s:
                ans.append(".".join(cur))
                return
            if (len(cur) == 4 and s) or not s: return

            dfs(s[1:], cur + [s[0]])
            if len(s) > 1 and s[0] != "0": dfs(s[2:], cur + [s[:2]])
            if len(s) > 2 and 100 <= int(s[:3]) <= 255:
                dfs(s[3:], cur + [s[:3]])

        dfs(s, [])
        return ans



