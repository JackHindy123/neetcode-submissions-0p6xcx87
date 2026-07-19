class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1 = {}
        for i, n in enumerate(nums): 
            x = target - n

            if (x in map1):
                return [map1[x], i]
            map1[n] = i