class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = []
        max_right = []
        min_height = []
        res = 0 
        max_l = 0
        max_r = 0
        for hgt in height:
            if max_l < hgt :
                max_l = hgt
            max_left.append(max_l)
        for i in range(len(height)-1,-1,-1):
            if max_r < height[i] :
                max_r = height[i]
            max_right.append(max_r)
        max_right = list(reversed(max_right))
        print(max_left)
        print(max_right)
        for i in range(len(height)):
            min_height.append(min((max_left[i],max_right[i])))
        for i in range(len(height)):
            temp = min_height[i] - height[i]
            print(temp)
            if temp > 0:
                res = res+ temp
        return res 

        

        