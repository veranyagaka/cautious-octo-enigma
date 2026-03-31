1class Solution:
2    def reductionOperations(self, nums: List[int]) -> int:
3        res = 0
4        steps = 0
5
6        nums.sort()
7
8        for i in range(1, len(nums)):
9            if nums[i] > nums[i-1]:
10                steps += 1
11            res += steps
12            # how far each no is from the minimum
13
14        return res