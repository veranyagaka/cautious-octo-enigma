1class Solution:
2    def pivotInteger(self, n: int) -> int:
3        nums = list(range(1, n+1))
4        left_sum = 0
5        total = sum(nums)
6
7        for i, x in enumerate(nums):
8            left_sum += x
9
10            total -= x # right sum
11            if total == left_sum - x: 
12                return x
13            
14
15        return -1