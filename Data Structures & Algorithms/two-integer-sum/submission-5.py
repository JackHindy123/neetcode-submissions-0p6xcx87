class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i in range(len(nums)):
            x = target - nums[i]

            if x in h:
                return [h[x], i]
            
            h[nums[i]] = h.get(nums[i], i)

            

