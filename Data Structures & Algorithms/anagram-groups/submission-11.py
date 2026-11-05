class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        bucket = {}
        for word in strs:
            if str(sorted(word)) in bucket:
                bucket[str(sorted(word))].append(word)
            else:
                bucket[str(sorted(word))] = [word]
            #print(word)
            #print(bucket),type(bucket[str(sorted(word))])
        #print(bucket.values())
        return list(bucket.values())
        