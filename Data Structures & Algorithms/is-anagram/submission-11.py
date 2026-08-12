class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #revision
        if len(s) != len(t):
            return False
        hmap_s = {}
        hmap_t = {}
        for c in s:
            if c in hmap_s:
                hmap_s[c] = hmap_s[c]+1
            else:
                hmap_s[c] = 1
        for c in t:
            if c in hmap_t:
                hmap_t[c] = hmap_t[c]+1
            else:
                hmap_t[c] = 1
        return hmap_s == hmap_t
        