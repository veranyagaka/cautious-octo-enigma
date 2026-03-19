1class Solution:
2    def balancedString(self, s: str) -> int:
3        n = len(s)
4        req = n // 4
5
6        l = 0
7        letters_over_limit = []
8
9        # counting how much each ch is repeated
10        counts = collections.Counter(s)
11        for ch, val in counts.items():
12            if val > req:
13                letters_over_limit.append(ch)
14
15        #edge case
16        if not letters_over_limit:
17            return 0
18
19        # sliding window
20        l = 0
21        res = float("infinity")
22         
23        for r in range(n):
24            counts[s[r]] -= 1
25
26            # valid window
27            while all(counts[ch] <= req for ch in letters_over_limit) and l <= r:
28                res = min(res, r -l + 1)
29                counts[s[l]] += 1
30                l += 1
31
32        return res
33