class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = []
        l.append(max(nums[:k]))
        left = 0
        for right in range(k,len(nums)):
            #move left and get new window
            left += 1
            l.append(max(nums[left:right+1]))

        return l

        