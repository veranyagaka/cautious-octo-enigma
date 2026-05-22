1class Solution:
2    def longestPalindrome(self, s: str) -> int:
3        
4        """
5        """
6        from collections import Counter
7        count = Counter(s)
8        total = 0
9        add = False
10
11        for c in count.values():
12            if c % 2 == 0:
13                total += c
14
15            else:
16                add = True ## for any odd count you can use 
17                total += c - 1
18
19        ## should we add a center character?
20        if add: total += 1
21        return total