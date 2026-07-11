class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                smaller_height = min(heights[i],heights[j])
                if max_water < smaller_height * (j-i):
                    max_water = smaller_height * (j-i)
        return max_water
        