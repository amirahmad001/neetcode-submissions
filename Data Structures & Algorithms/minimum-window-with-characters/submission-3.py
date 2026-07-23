class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        def idx(c):
            if c.isupper():
                return ord(c) - ord('A')
            return ord(c) - ord('a') + 26

        count1 = [0]*52
        count2 = [0]*52
        char_set = set()

        ans = ''

        for j in t:
            count1[idx(j)] += 1
            char_set.add(j)

        left = 0
        for j in range(len(s)):
            if s[j] in char_set:
                count2[idx(s[j])] += 1

            if all(count2[k] >= count1[k] for k in range(52)):
                while all(count2[k] >= count1[k] for k in range(52)):
                    if ans == "" or j - left + 1 < len(ans):
                        ans = s[left:j+1]

                    if s[left] in char_set:
                        count2[idx(s[left])] -= 1

                    left += 1

        return ans