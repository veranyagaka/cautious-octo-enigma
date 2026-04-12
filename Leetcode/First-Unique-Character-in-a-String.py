1class Solution:
2    def firstUniqChar(self, s: str) -> int:
3        from collections import Counter
4        count = Counter(s)
5
6        n = len(s)
7        ans = -1
8
9        for i in range(n):
10            if count[s[i]] == 1:
11                ans = i
12                break
13
14        return ans