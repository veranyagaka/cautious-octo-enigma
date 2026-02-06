1class Solution:
2    def areAlmostEqual(self, s1: str, s2: str) -> bool:
3        diff = []
4        n = len(s1)
5        for i in range(n):
6            if s1[i] != s2[i]:
7                diff.append(i)
8            
9        if len(diff) == 0:
10            return True
11
12        if len(diff) != 2:
13            return False
14
15        i, j = diff
16        return s1[i] == s2[j] and s1[j] == s2[i] 