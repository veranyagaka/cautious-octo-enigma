1class Solution:
2    def reverseString(self, s: List[str]) -> None:
3        """
4        Do not return anything, modify s in-place instead.
5        """
6        ## using recursion
7        def recurse(l, r):
8            if l < r:
9                recurse(l+1, r-1)
10                s[l], s[r] = s[r], s[l]
11
12        recurse(0, len(s) - 1)
13
14        