class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = [0] *52
        def idx(c):
            if c.isupper():
                return ord(c) - ord('A')
            return ord(c) - ord('a') + 26
        for ch in t:
            count[idx(ch)] += 1
        left = 0
        counter = 0
        s_string = ''
        for right in range(len(s)):
            if count[idx(s[right])] > 0:
                counter += 1
            count[idx(s[right])] -= 1
            while counter == len(t):
                #while count[idx(s[left])] <= 0:
                if s_string == '' or len(s[left:right+1]) < len(s_string):
                    s_string = s[left:right+1]
                count[idx(s[left])] += 1
                if  count[idx(s[left])] > 0 :
                    counter -= 1    
                left += 1     

        return s_string
        