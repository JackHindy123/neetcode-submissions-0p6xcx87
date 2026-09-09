class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        hashmap = {}
        hashmap2 = {}

        for i in range(len(s)):
            hashmap[s[i]] = hashmap.get(s[i], 0) + 1
            hashmap2[t[i]] = hashmap2.get(t[i], 0) + 1
                
        for n in hashmap:
            if hashmap[n] != hashmap2.get(n,0):
                return False

        return True
