class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hmap= {}
        i = 0
        w_length = 0
        max_w = 0
        for j in range(len(s)):
            if s[j] in hmap:
                hmap[s[j]] = hmap[s[j]]+1
            else:
                hmap[s[j]] = 1
            w_length += 1
            max_freq = max(hmap.values())
            print(max_freq,w_length)
            if w_length - max_freq <= k:
                print("if",j,i)
                max_w = max(max_w,w_length)
            else:
                print("else",s[j])
                hmap[s[i]] = hmap[s[i]]-1
                i += 1
                w_length -= 1
                
        return max_w
            
        