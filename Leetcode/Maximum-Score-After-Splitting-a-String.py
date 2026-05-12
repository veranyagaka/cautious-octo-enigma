1class Solution:
2    def maxScore(self, s: str) -> int:
3        
4        ## brute force
5
6        max_score = 0
7
8        for i in range(1, len(s)):
9            left = s[:i]
10            right = s[i:]
11
12            score = left.count("0") + right.count("1")
13
14            max_score = max(max_score, score)
15
16
17        return max_score