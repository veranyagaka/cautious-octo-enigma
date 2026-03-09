1class Solution:
2    def findContentChildren(self, g: List[int], s: List[int]) -> int:
3        ## using two pointers and sorting
4        g.sort()
5        s.sort()
6
7        no_of_children = len(g)
8        no_of_cookies = len(s)
9
10        res = 0
11
12        i, j = 0, 0
13
14        while i < no_of_children and j < no_of_cookies:
15            if g[i] <= s[j]:
16                res += 1
17                i += 1
18                j += 1
19
20            else:
21                j += 1
22
23        return res