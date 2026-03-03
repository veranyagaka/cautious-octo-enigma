1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        j = 0
7        for i in range(len(nums)):
8            if nums[i] != 0: # swap non zero elements
9                nums[i], nums[j] = nums[j], nums[i]
10                j += 1
11