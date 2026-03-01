1class Solution:
2    def reductionOperations(self, nums: List[int]) -> int:
3        nums.sort()
4        ops = 0
5        n = len(nums)
6        distinct_count = 0
7
8        for i in range(1, n):
9            if nums[i] != nums[i - 1]:
10                distinct_count += 1
11
12            ops += distinct_count
13
14
15        return ops
16
17        """nums = [5,1,3]
18        1,3,5
19
20
21        """