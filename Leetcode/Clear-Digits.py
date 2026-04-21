1class Solution:
2    def clearDigits(self, s: str) -> str:
3        stack = []
4        # i = 0
5
6        # while i < len(s):
7        #     ch = s[i]
8
9        for ch in s:
10            if ch.isdigit():
11                stack.pop()
12                continue
13            stack.append(ch)
14            # i += 1
15
16        return "".join(stack)