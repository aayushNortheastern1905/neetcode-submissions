class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack_result = []

        for token in tokens:
            if token not in "+-*/":
                stack_result.append(int(token))

            else:
                b = stack_result.pop()
                a = stack_result.pop()

                if token == "+":
                    stack_result.append(a+b)

                elif token == "-":
                    stack_result.append(a-b)

                elif token == "*":
                    stack_result.append(a*b)
                
                else:
                    stack_result.append(int(a/b))
        return stack_result[0]