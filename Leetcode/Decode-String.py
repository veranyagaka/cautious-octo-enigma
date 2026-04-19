1class Solution:
2    def decodeString(self, s: str) -> str:
3        curr_string = ""
4        stack = []
5        curr_num = 0
6
7        for c in s:
8            if c.isdigit():
9                curr_num = curr_num * 10 + int(c)
10
11            elif c == "[":
12                stack.append((curr_string, curr_num))
13                curr_string = ""
14                curr_num = 0
15
16
17            elif c == "]":
18                prev_string, num = stack.pop()
19                curr_string = prev_string + num * curr_string
20
21
22            else:
23                curr_string += c
24
25
26
27        return curr_string