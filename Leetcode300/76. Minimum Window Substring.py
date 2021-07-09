class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = Counter(t)
        valid = set()
        j,map,minL,ansI,ansJ= 0,{},len(s)+1,-1,-1
        for i in range(len(s)):
            map[s[i]] = map.get(s[i],0)+1
            if s[i] in count and map[s[i]] >=count[s[i]]: valid.add(s[i])
            while len(valid) == len(count):
                map[s[j]] -=1
                if s[j] in count and map[s[j]] < count[s[j]]:
                    valid.remove(s[j])
                    if i-j+1 < minL:
                        minL = i-j+1
                        ansI = i
                        ansJ = j
                j+=1
        return "" if minL == len(s)+1 else s[ansJ:ansI+1]