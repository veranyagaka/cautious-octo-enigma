1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        """the arr is sorted; duplicate elements together
4        in place modification
5        two pointers
6        one to keep track of curr element of original
7        second for unique elements"""
8
9        uniq = 0
10
11        for i in range(1, len(nums)):
12            if (nums[i] != nums[uniq]):
13                uniq += 1 # find the next uniq number
14            nums[uniq] = nums[i]
15
16        return uniq + 1 #index starts at zero; we need count of numbers