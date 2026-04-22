1class Solution:
2    ## binary search
3
4    def check(self, weights, limit, days):
5        ship_days = 1
6        total = 0
7
8        for w in weights:
9            total += w
10            if total > limit:
11                total = w
12                ship_days += 1
13
14        return ship_days <= days
15
16
17    def shipWithinDays(self, weights: List[int], days: int) -> int:
18
19        low, high = max(weights), sum(weights)
20
21        while low <= high:
22            mid = (low + high) // 2
23
24            if self.check(weights, mid, days):
25                ## go lower ie move the high pointer
26                high = mid - 1
27            
28            else:
29                low = mid + 1
30
31        return low
32
33
34    """
35    [1,2,3,4,5,6,7,8,9,10]
36    l = 10
37    h = 55
38    m = 32
39
40    ---
41
42
43
44
45    """
46