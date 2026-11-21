class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0

        longest = 0
        l, r = 0, len(heights) -1
        while l<r:
            area = min(heights[l], heights[r]) * (r-l)
            longest = max(longest, area)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return longest 