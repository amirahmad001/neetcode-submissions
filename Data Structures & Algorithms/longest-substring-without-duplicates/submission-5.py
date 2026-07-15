class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j,max_s = 0,0,0
        char_set = set()
        #char_set.add(s[0])
        while(j<len(s)):
            while s[j] in char_set:
                char_set.remove(s[i])
                i = i+1
            char_set.add(s[j])
            max_s = max(max_s,j-i+1)
            print(i,j)
            j += 1
        return max_s
        