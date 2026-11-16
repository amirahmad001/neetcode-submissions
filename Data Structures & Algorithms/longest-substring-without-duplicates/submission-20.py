class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l,r = 0,1
        max_l,curr_l = 1,1
        store = []
        store.append(s[l])
        while r < len(s):
            if s[r] not in store:
                store.append(s[r])
                r += 1
            else:
                curr_l = r - l
                max_l = max(max_l,curr_l)
                while store[0] != s[r]:
                    l = l+1
                    store.pop(0)
                store.pop(0)
                store.append(s[r])
                l += 1
                r += 1
            curr_l = r - l
            max_l = max(max_l,curr_l)
        return max_l

        