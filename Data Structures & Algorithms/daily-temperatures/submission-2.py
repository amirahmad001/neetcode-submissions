class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)-1,-1,-1):
            while len(st)>0 and temperatures[st[-1]] <= temperatures[i]:
                st.pop()
            if len(st) != 0:
                res[i] = st[-1] - i   
            #any case you need to push
            st.append(i)
        return res

        