class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        t_set = set(nums)
        seq = 0
        max_seq = 1 
        for i in nums:
            if i-1 not in t_set:
                print(i)
                seq = 1
                j=1
                while(seq != 0):
                    print("inside while:" ,i)
                    if i+j in t_set:
                        seq = seq+1
                        if seq > max_seq:
                            max_seq = seq
                        j = j+1
                    else:
                        seq = 0
        return max_seq
        