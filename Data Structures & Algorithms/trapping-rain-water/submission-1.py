class Solution:
    def trap(self, height: List[int]) -> int:
        left_max,right_max,tapped_water = 0,0,0
        left,right = 0, len(height) -1
        while left < right:
            if height[left] < height[right]:
                left_max = max(height[left],left_max)
                tapped_water += left_max - height[left]
                left += 1
            else:
                right_max = max(height[right],right_max)
                tapped_water += right_max - height[right]
                right -= 1
        return tapped_water

        