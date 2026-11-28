class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            remains = target - nums[i]
            if remains in hashmap:
                return [hashmap[remains],i]
            else:
                hashmap[nums[i]] = i
        return []
        