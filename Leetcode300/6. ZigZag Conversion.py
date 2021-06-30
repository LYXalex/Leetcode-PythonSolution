class Solution:

    # cycle
    def convert(self, s: str, numRows: int) -> str:
        levels = numRows * ['']
        port = numRows * 2 - 2
        for i in range(len(s)):
            if not port:
                levels[0] += s[i]
            elif i % port < numRows:
                levels[i % port] += s[i]
            else:
                levels[port - i % port] += s[i]
        res = ""

        for level in levels:
            res += level
        return res