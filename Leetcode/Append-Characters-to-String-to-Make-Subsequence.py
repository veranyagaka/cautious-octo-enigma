1class Solution:
2    def appendCharacters(self, s: str, t: str) -> int:
3        left, right = 0, 0
4        n, m = len(s), len(t)
5
6        while left < n and right < m:
7            if s[left] == t[right]:
8                right += 1
9            left += 1
10
11        ans = m - right # the remaining characters to make it a subsequence
12
13        return ans