1class Solution:
2    def repairCars(self, ranks: List[int], cars: int) -> int:
3        
4        ## supposed to use binary search
5
6        low = 1
7        high = max(ranks) * cars * cars
8
9        def is_possible(mid, ranks):
10            ## give the min and see how many cars they can repair
11            no = 0
12
13            for r in ranks:
14                no += int((mid / r) ** .5)
15
16            return no >= cars
17
18        while low <= high:
19            mid = (low + high) // 2
20
21            if is_possible(mid, ranks):
22                ## try a lower no
23                high = mid - 1
24
25            else:
26                low = mid + 1
27
28        return low
29