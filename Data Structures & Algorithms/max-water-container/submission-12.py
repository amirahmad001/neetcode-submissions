class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = -1
        i,j = 0,len(heights)-1
        while i < j:
            area = (j-i)*min(heights[i],heights[j])
            max_area = max(area,max_area)
            if heights[j] > heights[i]:
                i += 1
            else:
                j = j-1
        return max_area