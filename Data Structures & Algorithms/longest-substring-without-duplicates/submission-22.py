class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l,r = 0,1
        max_l,curr_l = 1,1
        store = set()
        store.add(s[l])
        while r < len(s):
            if s[r] not in store:
                store.add(s[r])
                r += 1
            else:
                curr_l = r - l
                max_l = max(max_l,curr_l)
                while s[l] != s[r]:
                    store.remove(s[l])
                    l = l+1
                l += 1
                store.add(s[r])
                r += 1
            curr_l = r - l
            max_l = max(max_l,curr_l)
        return max_l

        