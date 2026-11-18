class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_win = 0
        curr_win = 0
        l = 0
        freq = {}
        max_freq = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            max_freq = max(max_freq, freq[s[r]])
            if (r - l + 1) - max_freq > k:
                freq[s[l]] -= 1
                l += 1
            max_win = max(max_win, r - l + 1)
        return max_win
                

            

        