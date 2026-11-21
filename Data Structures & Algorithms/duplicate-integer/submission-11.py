class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h1 = {}

        for n in nums:
            if n in h1:
                return True
            else:
                h1[n] = h1.get(n, 1)
        return False