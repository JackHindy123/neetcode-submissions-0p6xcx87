class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        h = set(nums)

        longest = 0

        for n in h:
            if n-1 not in h:
                i = n
                length = 1
                while i+1 in h:
                    length+=1
                    i+=1

                longest = max(length, longest)
        return longest 