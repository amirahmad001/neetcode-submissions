class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}
        for num in nums:
            if num in store:
                store[num] += 1
            else:
                store[num] = 1
        s_v = dict(sorted(store.items(),key = lambda x : x[1],reverse = True))
        #print(list(s_v.keys())[:k])
        return list(s_v.keys())[:k]
        