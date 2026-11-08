class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        hashset = set(nums)
        longest = 0
        
        for n in hashset:
            length = 1
            if(n-1 not in hashset):
                i=n
                while (i+1 in hashset):
                    length+=1
                    i+=1
            longest = max(longest, length)
        return longest
            