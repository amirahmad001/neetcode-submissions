class Solution:
    def isPalindrome(self, s: str) -> bool:
        #x = s.lower()
        i = 0
        j = len(s)-1
        while (i<j):
            #print(x[i],x[j])
            if not s[j].isalnum():
                j -= 1
            elif not s[i].isalnum():
                i += 1
            elif s[i].lower() != s[j].lower():
                return False  
            else:
                i += 1
                j -= 1
        #print(x)
        return True
        