1class Solution:
2    def decodeString(self, s: str) -> str:
3
4        ## using recursion
5
6        def decode(i):
7            k = 0
8            result = ""
9
10            while i[0] < len(s):
11                ch = s[i[0]]
12
13                ## handling multidigits
14                if ch.isdigit():
15                    k = k * 10 + int(ch)
16
17                elif ch == "[":
18                    i[0] += 1
19                    inner = decode(i)
20                    result += inner * k
21                    k = 0 ## reset
22
23                elif ch == "]":
24                    return result
25
26                else:
27                    result += ch
28
29                i[0] += 1 # a pointer
30
31            return result
32
33        return decode([0])