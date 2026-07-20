class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j,l_sub = 0,1,0
        char_s = set()
        for j in range(len(s)):
            while s[j] in char_s : 
                char_s.remove(s[i])
                i = i+1
            char_s.add(s[j])
            l_sub = max(l_sub,j-i+1)
        return l_sub


        