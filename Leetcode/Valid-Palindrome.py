1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        # string preprocessing
4        s = "".join(ch.lower() for ch in s if ch.isalnum())
5
6        n = len(s)
7        l, r = 0, n -1
8
9        while l < r:
10            if s[l] != s[r]:
11                return False
12
13            l += 1
14            r -= 1
15
16        return True
17                