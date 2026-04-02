1class Solution:
2    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
3        # neetcode help
4
5        """
6        running sum
7        check the remainder - hashmap
8        remainder and the index
9        
10        if we find that the remainder already exists in the hashmap, we know that we have found the solution
11        23 % 6 = 5
12        25 % 6 = 1
13        29 % 6 = 5
14
15        ---
16        23 % 6 = 5
17        25 % 6 = 1
18        31 % 6 = 1
19        35 % 6 = 
20
21
22        so 2 and 4 is the good subarray
23        
24        i - remaider[i] > 1 ensure the length is at least 2"""
25
26        remainder = {0: -1}
27        total = 0
28
29        for i, n in enumerate(nums):
30            total += n
31            r = total % k
32
33            if r not in remainder:
34                remainder[r] = i
35
36            elif i - remainder[r] > 1:
37                return True
38
39        return False
40
41
42
43
44