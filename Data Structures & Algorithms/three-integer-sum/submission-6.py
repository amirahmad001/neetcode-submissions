class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hmap = {}
        for i in range(len(nums)):
            hmap[nums[i]] = i
        set_ = set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                
                two_sum = nums[i]+nums[j]
                diff = 0 - two_sum
                if diff in hmap and hmap[diff] != i and hmap[diff] != j:
                    print(i,j)
                    print(nums[i],nums[j])
                    l = [nums[i],nums[j],diff]
                    set_.add(tuple(sorted(l)))
        return list(set_)


        