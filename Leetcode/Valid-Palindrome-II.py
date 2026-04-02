1class Solution:
2    def validPalindrome(self, s: str) -> bool:
3        def isPalindrome(l, r):
4            while l < r:
5                if s[l] != s[r]:
6                    return False
7
8                l += 1
9                r -= 1
10
11            return True
12
13        # already a palindrome
14        n = len(s)
15        l = 0
16        r = n -1
17
18        while l < r:
19            if s[l] != s[r]:
20                return isPalindrome(l+1, r) or isPalindrome(l, r-1) # one mismatch allowed; we are moving the left pointer or the right pointer; 2 conditions
21
22            l += 1
23            r -= 1
24
25        return True