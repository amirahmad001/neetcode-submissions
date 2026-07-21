class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        count1 = [0]*26
        count2 = [0]*26
        for ch in s1:
            count1[ord(ch)-ord('a')] = count1[ord(ch)-ord('a')] +1
        for i in range(0,len(s1)):
            count2[ord(s2[i])-ord('a')] = count2[ord(s2[i])-ord('a')] +1
        if count1 == count2:
            return True
        left = 0
        print(count1)
        print("count 2")
        for right in range(len(s1),len(s2)):
            #add one element 
            count2[ord(s2[right])-ord('a')] = count2[ord(s2[right])-ord('a')] +1

            #remove left
            count2[ord(s2[left])-ord('a')] = count2[ord(s2[left])-ord('a')] -1
            left += 1

            #compare if in current window it matches
            print(count2)
            if count1 == count2:
                return True


        print(count1)
        return False
        