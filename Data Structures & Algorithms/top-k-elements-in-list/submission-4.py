class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        l = []
        for num in nums:
            if num in hmap:
                hmap[num] += 1
            else:
                 hmap[num] = 1
        sorted_values= dict(sorted(hmap.items(),key = lambda x: x[1],reverse = True))
        l = list(sorted_values.keys())
        return l[:k]
        