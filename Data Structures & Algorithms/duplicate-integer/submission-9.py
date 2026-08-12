class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #revision
        hashmap = {}
        for num in nums:
            if num in hashmap:
                return True
            else:
                hashmap[num] = 1
        return False
        