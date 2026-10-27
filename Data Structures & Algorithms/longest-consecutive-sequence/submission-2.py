class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)

        longest = 0
        
        for n in hashset: 
            if n-1 not in hashset:
                length = 1
                x = n
                while x+1 in hashset:
                    length+=1
                    x+=1
                longest = max(longest, length)
        return longest