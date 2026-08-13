class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #revision
        store = {}
        for st in strs:
            if str(sorted(st)) in store:
                store[str(sorted(st))].append(st)
            else:
                store[str(sorted(st))] = [st]
        return list(store.values())      