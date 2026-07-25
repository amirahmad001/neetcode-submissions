class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for ch in s:
            if not st or  ch == '(' or ch == '{' or ch == '[':
                st.append(ch)
            elif st and  ch == ')' and st[-1] == '(':
                st.pop()
            elif st and ch == '}' and st[-1] == '{':
                st.pop()
            elif st and ch == ']' and st[-1] == '[':
                st.pop()
            else:
                st.append(ch)

        print(not st,st)
        return not st


        