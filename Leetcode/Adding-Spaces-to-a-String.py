1class Solution:
2    def addSpaces(self, s: str, spaces: List[int]) -> str:
3        res = []
4        n = len(s)
5        spaces = set(spaces)
6
7        for i in range(n):
8            if i in spaces:
9                res.append(" ")
10
11            res.append(s[i])
12
13
14        return "".join(res)
15        