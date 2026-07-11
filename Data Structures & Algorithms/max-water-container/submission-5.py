class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r,max_water = 0, len(heights) - 1,0
        while(l<r):
            max_water = max(min(heights[l],heights[r]) * (r-l),max_water)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_water

        