1class Solution:
2    def evalRPN(self, tokens: List[str]) -> int:
3        stack = []
4        ops = ["*", "/", "+", "-"]
5        
6        for ch in tokens:
7            if ch in ops:
8
9                operand1 = stack.pop() # ordering of this matters btw
10                operand2 = stack.pop()
11
12                if ch == "*":
13                    ans = operand2 * operand1
14                elif ch == "/":
15                    ans = int(operand2 / operand1) # towards zero no float
16
17                elif ch == "+":
18                    ans = operand2 + operand1
19                else:
20                    ans = operand2 - operand1
21                stack.append(ans)
22
23            else:
24                stack.append(int(ch)) # this just adds the no to the stack
25
26        return stack[0]