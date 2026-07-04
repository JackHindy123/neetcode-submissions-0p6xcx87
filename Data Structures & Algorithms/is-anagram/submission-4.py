class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s)!=len(t)):
            return False
        
        map1 = {}
        map2 = {}

        for i in range(len(s)):
            char1 = s[i]
            char2 = t[i]
            
            if (char1 in map1):
                map1[char1] += 1
            else:
                map1[char1] = 1
            if (char2 in map2):
                map2[char2] += 1
            else:
                map2[char2] = 1
        if (map1 == map2):
            return True
        return False