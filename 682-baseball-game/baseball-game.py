class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for i in operations:
            match(i):
                case'+':
                    op1=stack[-1]
                    op2=stack[-2]
                    stack.append(op1+op2)
                case'D':
                    op=stack[-1]
                    stack.append(2*op)
                case'C':
                    stack.pop()
                case _:
                    stack.append(int(i))
            sum1=0
            if stack:
                sum1=sum(stack)
        return sum1

        