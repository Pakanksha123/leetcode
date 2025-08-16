class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        oper=['+','-','*','/']
        for i in tokens:
            if i not in oper:
                st.append(int(i))
            else:
                num2=st.pop()
                num1=st.pop()
                if i=='*':
                    st.append(num2*num1)
                elif i=='+':
                    st.append(num1+num2)
                elif i=='-':
                    st.append(num1-num2)
                elif i=='/':
                    st.append(int(num1/num2))
        return st[-1]


        