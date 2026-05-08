1class Solution:
2    def maximumCandies(self, candies: List[int], k: int) -> int:
3
4        ## edge case, there is not enough candies return o
5
6        if sum(candies) < k:
7            return 0
8        
9        low = 1
10        high = max(candies)
11
12        def is_possible(mid, candies):
13            child = 0
14
15            for x in candies:
16                child += (x // mid)
17
18            return child >= k
19
20
21        while low <= high:
22            mid = (low + high) // 2
23
24            if is_possible(mid, candies):
25
26                ##try a higher number
27                low = mid + 1
28
29            else:
30                high = mid - 1
31
32        return high