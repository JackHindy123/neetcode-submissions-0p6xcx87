class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map1 = {}

        for n in nums:
            if n not in map1:
                map1[n] = 0
            else:
                return True

        return False