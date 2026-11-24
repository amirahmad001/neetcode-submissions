class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_size,max_freq,win_size = 0,0,0
        store = {}
        for r in range(len(s)):
            if s[r] in store:
                store[s[r]] = store[s[r]] + 1
            else:
                 store[s[r]] = 1

            max_freq = max(max_freq,store[s[r]])

            win_size = r-l +1
            if win_size - max_freq > k:
                store[s[l]] -= 1
                l += 1
                win_size -= 1
            max_size = max(max_size,win_size)
        return max_size
        