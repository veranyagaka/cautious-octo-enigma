1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        """the arr is sorted; duplicate elements together
4        in place modification
5        two pointers
6        one to keep track of curr element of original
7        second for unique elements"""
8
9        uniq = 0
10        n = len(nums)
11
12        for i in range(1, n):
13            if nums[i] != nums[uniq]:
14                uniq += 1 # find the next uniq number
15            nums[uniq] = nums[i]
16
17        return uniq + 1 #index starts at zero; we need count of numbers