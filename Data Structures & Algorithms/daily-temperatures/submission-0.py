class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = []
        is_Added = False
        for i in range(len(temperatures)):
            for j in range(i+1,len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    res.append(j-i)
                    is_Added = True
                    break
            if is_Added == False:
                res.append(0)
            else:
                is_Added = False
            
        return res

            