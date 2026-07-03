class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoMap = {}
        
        for i, n in enumerate(nums):
            x = target - n
            
            if(x in twoMap):
                return [twoMap[x], i]
            
            twoMap[n] = i