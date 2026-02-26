1class Solution:
2    def sortColors(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        dutch national flag
6        """
7        low, mid, high = 0, 0, len(nums)-1
8
9        while mid <= high:
10            if nums[mid] == 0:
11                nums[low], nums[mid] = nums[mid], nums[low]
12                low += 1
13                mid += 1
14
15            elif nums[mid] == 1:
16                mid += 1
17
18            else:
19                nums[mid], nums[high] = nums[high], nums[mid]
20                high -= 1
21        