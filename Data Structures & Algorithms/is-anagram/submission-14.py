class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm_s = {}
        hm_t = {}
        for i in s:
            if i in hm_s:
                hm_s[i] += 1
            else:
                 hm_s[i] = 1
        for i in t:
            if i in hm_t:
                hm_t[i] += 1
            else:
                 hm_t[i] = 1
        return hm_s == hm_t
        