class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        map1 = {}

        for string in strs: 
            if "".join(sorted(string)) in map1:
                map1["".join(sorted(string))].append(string)
            else:
                map1["".join(sorted(string))] = [string]
           
            
        return list(map1.values())