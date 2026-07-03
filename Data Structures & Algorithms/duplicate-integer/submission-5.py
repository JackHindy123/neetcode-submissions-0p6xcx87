class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map1 = {}

        for n in nums:
            if (n in map1):
                return True
            
            map1[n] = 0
        return False
        


