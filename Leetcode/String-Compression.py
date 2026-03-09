1from typing import List
2
3class Solution:
4    def compress(self, chars: List[str]) -> int:
5        # two pointers
6
7        n = len(chars)
8        w = 0        
9        i = 0
10
11        while i < n:
12            j = i
13
14            while  j < n and chars[j] == chars[i] :
15                j += 1
16
17            count = j -i
18            chars[w] = chars[i]
19            w += 1
20
21            if count > 1:
22                for c in str(count):
23                    chars[w] = c
24                    w += 1
25
26            i = j
27        
28        return w