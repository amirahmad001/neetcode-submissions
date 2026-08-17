class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        max_l = 1
        curr_l = 1
        nums.sort()
        nums = list(sorted(set(nums)))
        #print(nums)
        for i in range(len(nums)):
            if i == 0:
                curr_l = 1
            if nums[i] == nums[i-1] +1:
                curr_l += 1
                max_l = max(curr_l,max_l)
                #print("yes-> ",nums[i])
            else:
                curr_l = 1
        return max_l


        