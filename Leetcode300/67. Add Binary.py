class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a ,b = a[::-1], b[::-1]
        i,j,t,ans = 0,0,0,""
        while i < len(a) or j < len(b):
            if i < len(a):
                t += int(a[i])
                i+=1
            if j < len(b):
                t += int(b[j])
                j +=1
            ans += str(t%2)
            t = t//2
        if t: ans+= str(t)
        return ans[::-1]