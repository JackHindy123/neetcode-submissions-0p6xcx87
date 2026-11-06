class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        
        hashset = set(nums)
        longest = 0

        for n in hashset:
            if (n-1) not in hashset:
                i = n
                length = 1
                while (i+1 in hashset): 
                    i+=1
                    length+=1
                longest = max(longest, length)
        return longest