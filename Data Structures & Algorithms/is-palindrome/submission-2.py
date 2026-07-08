class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = s.lower()
        i = 0
        j = len(s)-1
        while (i<j):
            print(x[i],x[j])
            if x[i].isalnum() and x[j].isalnum():
                if x[i] != x[j]:
                    print(i,j) 
                    return False
                else:
                    i += 1
                    j -= 1
            elif x[i].isalnum() and not x[j].isalnum():
                j -= 1
            elif x[j].isalnum() and not x[i].isalnum():
                i += 1
            else:
                i += 1
                j -= 1
        print(x)
        return True
        