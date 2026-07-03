class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map1 = {}

        for i in range(len(strs)):
            string = "".join(sorted(strs[i]))

            if string not in map1:
                map1[string] = [strs[i]]
            else:
                map1[string].append(strs[i])
        return list(map1.values())
