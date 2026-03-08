1class Solution:
2    def thirdMax(self, nums: List[int]) -> int:
3        """
4        the third distinct max no: we need a set
5        if the third no is not availble return the max no"""
6        nums = sorted(list(set(nums)))[::-1]
7
8        if len(nums) < 3:
9            return max(nums)
10
11        return nums[2]
12