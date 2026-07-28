class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        
        i = 0 

        for x in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if (j!=i):
                    prod *= nums[j]
            output.append(prod)
            i+=1
        return output
