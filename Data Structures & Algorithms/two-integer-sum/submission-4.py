class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h1 = {}

        for i in range(len(nums)):
            x = target - nums[i]
            
            if (x in h1):
                return [h1[x], i]
            h1[nums[i]] = h1.get(nums[i], i)