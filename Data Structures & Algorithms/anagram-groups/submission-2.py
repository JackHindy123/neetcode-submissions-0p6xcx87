class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map1 = {}

        for n in strs:
            st = "".join(sorted(n))
            if (st in map1):
                map1[st].append(n)
            else:
                map1[st] = [n]
        
        return list(map1.values())

        