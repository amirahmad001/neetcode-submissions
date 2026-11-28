class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = {}
        for char in s:
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 1
        print(hashmap)
        for char in t:
            if char in hashmap:
                hashmap[char] -= 1
            else:
                hashmap[char] = 1
        print(hashmap)
        for res in hashmap:
            if hashmap[res] > 0:
                return False
        return True
        