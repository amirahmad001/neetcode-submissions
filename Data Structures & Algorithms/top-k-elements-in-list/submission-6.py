class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}
        for num in nums:
            if num in store:
                store[num] = store[num]+1
            else:
                store[num] = 1
        #print(store)
        store = dict(sorted(store.items(),key = lambda x: x[1],reverse = True))
        #print()
        return list(store.keys())[:k]
        