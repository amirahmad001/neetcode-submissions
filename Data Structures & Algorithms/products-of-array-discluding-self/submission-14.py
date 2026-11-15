class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref_prd = []
        post_prd = []
        p_prd = 1
        po_prd = 1
        ans = []
        for i in range(len(nums)):
            p_prd = p_prd*nums[i]
            pref_prd.append(p_prd)
        #print(pref_prd)
        for i in range(len(nums)-1,-1,-1):
            po_prd = po_prd*nums[i]
            post_prd.append(po_prd)
        #print(list(reversed(post_prd)))
        post_prd = list(reversed(post_prd))
        for i in range(len(nums)):
            if i > 0 and i < len(nums)-1:
                prd = pref_prd[i-1] * post_prd[i+1]
                ans.append(prd)
            elif i > 0:
                prd = pref_prd[i-1]
                ans.append(prd)
            else:
                prd = post_prd[i+1]
                ans.append(prd)
        return ans