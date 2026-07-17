class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i,j = 0,0
        max_window = 0
        window_size = 0
        l = len(s)
        hmap = {}
        while j < len(s):
            if s[j] in hmap:
                hmap[s[j]] = hmap[s[j]] + 1
                            
            else:
                hmap[s[j]] = 1
                
            max_freq = max(hmap.values())
            print(window_size,max_freq)
            window_size += 1
            if window_size  - max_freq <= k:
                max_window = max(max_window, window_size)
                j = j+1
            else:
                hmap[s[i]] = hmap[s[i]] - 1
                i = i+1
                window_size -= 1
                max_freq = max(hmap.values())
                j += 1
        
        return max_window



        