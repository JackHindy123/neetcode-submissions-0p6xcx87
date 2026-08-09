class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {}

        for char in s:
            map1[char] = map1.get(char, 0) + 1

        for char in t:
            if char not in map1: 
                return False
            else:
                map1[char] = map1.get(char, 0) - 1
                
        if all(values == 0 for values in map1.values()):
            return True
        return False