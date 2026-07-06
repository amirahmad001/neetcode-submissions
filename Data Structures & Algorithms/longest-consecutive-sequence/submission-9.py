class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_list = list(sorted(set(nums)))
        if(len(nums)) == 0:
            return 0
        print(sorted_list)
        max_ = 0
        max_seq = 1
        for i in range(len(sorted_list)):
            if i == 0:
                print(i,"0")
                max_ = 1
            elif sorted_list[i] == sorted_list[i-1] + 1:
                max_ += 1
                print(i,"1",max_)
            else:
                print(max_ > max_seq)
                if max_ > max_seq:
                    max_seq = max_
                max_ = 1
                print(i,"2",max_seq)
        return max_seq if max_seq > max_ else max_
        