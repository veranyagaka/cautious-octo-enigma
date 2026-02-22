1class Solution:
2    def binaryGap(self, n: int) -> int:
3        bin_no = bin(n)[2:]
4        prev = None
5        max_dist = 0
6
7        for i, ch in enumerate(bin_no):
8            if ch == "1":
9                if prev is not None:
10                    max_dist = max(max_dist, i -prev)
11                prev = i
12
13        return max_dist