class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #revision
        return len(set(nums)) != len(nums)
        