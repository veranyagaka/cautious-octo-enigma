1class Solution:
2    def countBinarySubstrings(self, s: str) -> int:
3        subs = 0
4        n = len(s)
5        count = 1
6        res = []
7        ## groups
8        for i in range(1, n):
9            if s[i] == s[i - 1]:
10                count += 1
11            else:
12                res.append(count)
13                count = 1  # reset
14
15        res.append(count) # last group
16
17        for j in range(len(res) -1):
18            subs += min(res[j],res[j+1])
19
20        return subs