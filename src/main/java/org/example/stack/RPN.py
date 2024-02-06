class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for t in tokens:
            match t:
                case "+":
                    stack.append(stack.pop() + stack.pop())
                case "-":
                    a, b = stack.pop(), stack.pop()
                    stack.append(b - a)
                case "*":
                    stack.append(stack.pop() * stack.pop())
                case "/":
                    a, b = stack.pop(), stack.pop()
                    stack.append(int(b / a))
                case _:
                    stack.append(int(t))
        return stack[0]


obj = Solution()
# tokens = ["2","1","+","3","*"]
# tokens = ["4","13","5","/","+"]
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(obj.evalRPN(tokens))
