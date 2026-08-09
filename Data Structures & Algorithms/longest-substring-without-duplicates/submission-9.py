class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j,l_sub = 0,1,0
        char_ = set()
        for j in range(len(s)):
            while s[j] in char_ : 
                char_.remove(s[i])
                i = i+1
            char_.add(s[j])
            l_sub = max(l_sub,j-i+1)
        return l_sub


        