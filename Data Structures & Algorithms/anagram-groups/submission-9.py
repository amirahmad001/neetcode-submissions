class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}
        for s in strs:
            if str(sorted(s)) in store:
                store[str(sorted(s))].append(s)
            else:
                store[str(sorted(s))] = [s]
        values = store.values()
        #print(values)
        return list(values)
        