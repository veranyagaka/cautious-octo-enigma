1class Solution:
2    def minEatingSpeed(self, piles: List[int], h: int) -> int:
3
4        low = 1
5        high = max(piles)
6
7
8        while low <= high:
9            # what does mid represent - speed
10            mid = (low + high) // 2
11
12            ## try with this speed
13            total = 0
14            for p in piles:
15                total += (p+mid-1) // mid
16
17
18            if total <= h:
19                high = mid - 1
20
21            else:
22                low = mid + 1
23
24        return low
25
26
27        """
28        speed and time
29        mid represent speed that means bananas eaten should be
30
31
32        returning k
33        approach
34
35        [30,11,23,4,20]
36        5 hrs
37        6 hrs
38
39
40        not possible - constraints
41        2hr
42        
43        example testcase
44        piles = [3,6,7,11], h = 8
45        ans = 4
46
47        """