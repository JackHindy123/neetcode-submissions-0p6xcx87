class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ct = {}
        freq = [[] for i in range(len(nums) + 1)]

        for i in range(len(nums)):
            ct[nums[i]] = ct.get(nums[i], 0) + 1
        
        for c, n in ct.items():
            freq[n].append(c)
    
        
        res = []
        for i in range(len(freq) -1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
