class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h = set(nums)

        longest = 0

        for n in h: 
            if n-1 not in h:
                length = 1
                i = n + 1
                while i in h:
                    length+=1
                    i+=1
                longest = max(longest, length)
        return longest