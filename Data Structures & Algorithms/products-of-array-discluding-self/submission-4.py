class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prd = []
        right_prd = []
        l_prd = 1
        r_prd = 1
        for num in nums:
            l_prd *= num 
            left_prd.append(l_prd)
        print(left_prd)
        for i in range(len(nums)-1,-1,-1):
            r_prd *= nums[i]
            right_prd.append(r_prd)
        right_prd.reverse()
        print(right_prd)
        l = []
        for i in range(len(nums)):
            prd = 1
            if i == 0 and i < len(nums):
                prd = right_prd[i+1]
            elif i == len(nums)-1:
                prd = left_prd[i-1]
            else:
                prd = left_prd[i-1] * right_prd[i+1]
            l.append(prd)
        return l
        