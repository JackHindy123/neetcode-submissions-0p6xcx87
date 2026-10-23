class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h1 = {}

        for s in strs:
            key = "".join(sorted(s))
            if key not in h1:
                h1[key] = h1.get(key, [])
            h1[key].append(s)
        
        return list(h1.values())


