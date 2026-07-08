class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = s.lower()
        i = 0
        j = len(s)-1
        while (i<j):
            #print(x[i],x[j])
            if not x[j].isalnum():
                j -= 1
            elif not x[i].isalnum():
                i += 1
            elif x[i] != x[j]:
                return False  
            else:
                i += 1
                j -= 1
        #print(x)
        return True
        