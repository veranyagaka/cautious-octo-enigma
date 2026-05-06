1class Solution:
2    def isMatch(self, s: str, p: str) -> bool:
3
4        @cache
5        def dfs(i, j):
6            if j == len(p):
7                return i == len(s) ## we have consumed the entire string
8
9            m = i < len(s) and (p[j] == s[i] or p[j] == ".")
10            # check whether the current char matches or . (any single character)
11            # only valid if it has not passed the len(s)
12
13            ## two cases
14            # we can either
15            # skip the curr occurence ie d*abs and abs
16            ## use the curr occurence one or more times
17
18            if j + 1 < len(p) and p[j+1] == "*":
19                res = dfs(i, j+2) or (m and dfs(i+1, j)) 
20
21            else:
22                res = m and dfs(i+1, j+1)
23
24            ## otherwise we check whether equal and move on to the next chars
25            
26
27            
28
29            return res
30
31
32
33        return dfs(0, 0)
34
35        """
36        wheter s[i:] matches p[j:]
37
38        """