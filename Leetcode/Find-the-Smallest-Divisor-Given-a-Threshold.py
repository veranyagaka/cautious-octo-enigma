1class Solution:
2    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
3        
4        ## using binary search
5        import math
6        low = 1
7        high = max(nums)
8
9        while low <= high:
10            mid = (low+high) // 2
11            ## mid is the divisor
12            total = 0
13
14            for x in nums:
15                total += math.ceil(x/mid)
16                
17            # print(total)
18            if total > threshold:
19                low = mid + 1
20
21            else:
22                high = mid - 1
23
24
25        ## what tdo we return 
26        return low
27
28        """
29        nums = [1,2,5,9], threshold = 6
30        low = 0
31        high = 17
32
33        mid = 8
34
35        total = 5
36        high = 17
37        low = 9
38        --- 
39        low = 0
40        high = 7
41
42
43        """
44