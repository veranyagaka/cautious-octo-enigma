1class Solution:
2    def longestSemiRepetitiveSubstring(self, s: str) -> int:
3        left = 0
4        best = 1
5        n = len(s)
6        count = 0
7
8        for right in range(1, n):
9            if s[right] == s[right - 1]:
10                count += 1
11
12            while count > 1:
13                if s[left] == s[left + 1]:
14                    count -= 1
15                left += 1
16
17            best = max(best, right - left + 1)
18
19        return best