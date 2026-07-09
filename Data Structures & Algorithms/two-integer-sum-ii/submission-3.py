class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(len(numbers)):
            hmap[numbers[i]] = i
        for i in range(len(numbers)):
            remaining = target - numbers[i]
            if remaining in hmap:
                if hmap[remaining] > i :
                    return [i+1,hmap[remaining]+1]
        return []

        