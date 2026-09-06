class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_nums = list(sorted(set(nums)))
        curr_l = 0
        max_l = 0
        for i in range(len(new_nums)):
            if i == 0:
                curr_l = 1
            elif new_nums[i] == new_nums[i-1]+1:
                curr_l += 1
            else:
                #max_l = max(max_l,curr_l)
                curr_l = 1
            max_l = max(max_l,curr_l)
        return max_l
            