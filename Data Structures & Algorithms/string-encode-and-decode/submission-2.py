class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s

        return result
        
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        arrayIdx = 0
        while len(s) != i:
            wordLen = ""
            while s[i] != "#":
                wordLen+=s[i]
                i+=1
            wordLen = int(wordLen)
            i+=1
            result.append("")
            for j in range(wordLen):
                result[arrayIdx]+= s[i]
                i+=1
            arrayIdx+=1
        
        return result 

            
            
        
