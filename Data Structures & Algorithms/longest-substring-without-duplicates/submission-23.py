class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 1
        max_length = 1
        seen = {s[0]} if s else set()

        if not s:
            return 0

        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                right += 1
            else:
                while s[left] != s[right]:
                    seen.remove(s[left])
                    left += 1

                left += 1
                seen.add(s[right])
                right += 1

            max_length = max(max_length, right - left)

        return max_length