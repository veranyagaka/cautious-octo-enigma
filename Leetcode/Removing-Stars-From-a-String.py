1class Solution:
2    def removeStars(self, s: str) -> str:
3        stack = []
4        for ch in s:
5            if ch == "*":
6                if stack:
7                    stack.pop()
8
9            else:
10                stack.append(ch)
11
12        return "".join(stack)
13        """
14        approach if you encounter a * and there are elements in the stack
15        you pop period
16        """