class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_l = 1
        l = 0
        store = set()
        if not s:
            return 0
        else:
            store.add(s[0])
        for r in range(1,len(s)):
            if s[r] not in store:
                store.add(s[r])
            else:
                while s[l] != s[r]:
                    store.remove(s[l])
                    l = l+1
                l += 1
                store.add(s[r])
            max_l = max(max_l,r-l+1)
            #print(max_l,s[l],s[r])
        return max_l
        