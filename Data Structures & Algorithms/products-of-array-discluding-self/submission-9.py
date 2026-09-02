class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #revision
        pref_prd = []
        post_prd = [0] * len(nums)
        ans = [0]* len(nums)
        pf_prd = 1
        pst_prd = 1
        for num in nums:
            pf_prd *= num
            pref_prd.append(pf_prd)
        #print(pref_prd)

        for i in range(len(nums)-1,-1,-1):
            pst_prd *= nums[i]
            post_prd[i] = pst_prd
        #print(post_prd)

        for i in range(len(nums)):
            if i == 0:
                ans[i] = post_prd[i+1]
            elif i == len(nums)-1:
                ans[i] = pref_prd[i-1]
            else:
                ans[i] = post_prd[i+1] * pref_prd[i-1]
        #print(ans)
        return ans



        