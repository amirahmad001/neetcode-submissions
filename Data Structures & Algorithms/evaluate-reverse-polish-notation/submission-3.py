class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        st = []
        operator = ['+','-','*','/']
        res = 0
        for elem in tokens:
            if elem in operator:
                b = st.pop()
                a = st.pop()
                res = self.evaluate(a,b,elem)
                st.append(res)
            else:
                st.append(elem)
        return res

    def evaluate(self,a,b,operator):
        print(a,b,operator)
        if operator == '+':
            return int(a)+int(b)

        if operator == '-':
            return int(a)-int(b)

        if operator == '*':
            return int(a)*int(b)
        if operator == '/':
            return int(int(a) / int(b))
        