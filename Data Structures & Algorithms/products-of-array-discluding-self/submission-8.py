class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = [1] * len(nums)

        pre = 1 
        for i in range(len(nums)):
            a[i] = pre 
            pre*=nums[i]
        
        post = 1 
        for i in range(len(nums)-1, -1, -1):
            a[i] *= post
            post*= nums[i]

        return a
