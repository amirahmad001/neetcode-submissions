class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #revision
        return sorted(s) == sorted(t)
        