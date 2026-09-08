class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            two_sum_ = self.twoSum(i+1,nums,-(nums[i]))
            for pair in two_sum_:
                ans.append([nums[i]] + pair)
        return ans

    def twoSum(self,i,nums,target):
        j = len(nums)-1
        ans = []
        while(i<j):
            if nums[i] + nums[j] > target:
                j = j-1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                ans.append([nums[i],nums[j]])
                while i < j and nums[i] == nums[i + 1]:
                    i += 1

                # Skip duplicate right values
                while i < j and nums[j] == nums[j - 1]:
                    j -= 1
                i = i+1
                j = j-1
        return ans