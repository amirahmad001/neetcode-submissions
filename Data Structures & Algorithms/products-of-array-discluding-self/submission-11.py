class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preff_prd = [0 for i in range(len(nums))]
        pref_prd = 1
        suff_prd = [0 for i in range(len(nums))]
        suf_prd = 1
        ans = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            pref_prd *=  nums[i]
            #print(i,len(preff_prd))
            preff_prd[i] = pref_prd
        for i in range(len(nums)-1,-1,-1):
            suf_prd *=  nums[i]
            #print(i,suf_prd,nums[i])
            suff_prd[i] = suf_prd
        #print(suff_prd)
        #print(preff_prd)
        for i in range(len(nums)):
            if i == 0:
                ans[i] = suff_prd[i+1]
            elif i == len(nums)-1:
                ans[i] = preff_prd[i-1]
            else:
                ans[i] = preff_prd[i-1] * suff_prd[i+1]
        return ans




        