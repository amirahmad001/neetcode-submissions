class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket= {}
        for num in nums:
            if num in bucket:
                bucket[num] = bucket[num]+1
            else:
                bucket[num] = 1
        #print(bucket)
        ans = dict(sorted(bucket.items(),key = lambda x : x[1],reverse = True)).keys()
        #print(ans)
        return list(ans)[:k]
        