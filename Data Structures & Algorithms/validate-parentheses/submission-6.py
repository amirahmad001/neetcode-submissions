class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for ch in s:
            if st and  ch == ')' and st[-1] == '(':
                st.pop()
            elif st and ch == '}' and st[-1] == '{':
                st.pop()
            elif st and ch == ']' and st[-1] == '[':
                st.pop()
            else:
                st.append(ch)
        print(not st,st)
        return not st


        