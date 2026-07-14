class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_ = set()
        l= 0
        max_k = 0

        for r in range(len(s)):
            while s[r] in set_:
                print("in while",l,s[l])
                set_.remove(s[l]) 
                l = l+1
            set_.add(s[r])
            print(l,s[l],r,s[r])
            max_k = max(max_k,r-l + 1)
        return max_k
        