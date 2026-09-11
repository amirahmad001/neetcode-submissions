class Solution:
    def trap(self, height: List[int]) -> int:
        left_highest = [0]*len(height)
        right_highest = [0]*len(height)
        l_max = 0
        r_max = 0
        for i in range(len(height)):
            l_max = max(l_max,height[i])
            left_highest[i] = l_max
        for i in range(len(height)-1,-1,-1):
            r_max = max(r_max,height[i])
            right_highest[i] = r_max
        #print(left_highest)
        #print(right_highest)
        ans = 0
        for i in range(len(height)):
            #print("ith -> ",i)
            if i == 0 or i == len(height) -1:
                continue
            else:
                #print(ans, min(left_highest[i-1],right_highest[i+1]),height[i])
                water_tap = min(left_highest[i-1],right_highest[i+1]) - height[i]
                if water_tap > 0:
                    ans = ans+water_tap
        return ans
        

