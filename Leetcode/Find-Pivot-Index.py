1class Solution:
2    def pivotIndex(self, nums: List[int]) -> int:
3        total_sum = sum(nums)
4        left_sum = 0
5
6        for i in range(len(nums)):
7
8            if left_sum == total_sum - left_sum - nums[i]:
9                return i
10
11            left_sum += nums[i]
12
13        return -1