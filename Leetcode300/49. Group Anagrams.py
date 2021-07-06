class Solution:
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        ans, map = [], defaultdict(list)
        for i, word in enumerate(strs):
            sorted_word = "".join(sorted(list(word)))
            map[sorted_word].append(word)
        for _, val in map.items():
            ans.append(val)
        return ans

    # tuple is allowed for the key of dictionary
    def groupAnagrams(self, strs):
        d = {}
        for w in strs:
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return d.values()

