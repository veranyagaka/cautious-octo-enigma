1class Solution:
2    def singleNonDuplicate(self, nums: List[int]) -> int:
3
4        l = 0
5        r = len(nums) - 1
6
7        if len(nums) == 1:
8            return nums[0]
9
10        while nums[l] == nums[l + 1] and nums[r - 1] == nums[r]:
11            l += 2
12            r -= 2
13
14        if nums[l] != nums[l + 1]:
15            return nums[l]
16
17        if nums[r] != nums[r - 1]:
18            return nums[r]
19        
20        # ## neetcode help
21        # l = 0
22        # r = len(nums) - 1
23
24        # if len(nums) == 1:
25        #     return nums[0]
26
27        # while l <= r:
28
29        #     m = (l + r) // 2
30
31        #     # while m is in bounds
32        #     if m - 1 >= 0 and m + 1 < len(nums):
33        #         if nums[m - 1] != nums[m] and  nums[m + 1] != nums[m]:
34        #             return nums[m]
35
36        #     if nums[m-1] == nums[m]:
37        #         leftSide = m - 1
38
39        #     else:
40        #         leftSide = m 
41
42
43        #     if leftSide % 2:
44        #         r = m - 1
45
46
47        #     else:
48        #         l = m + 1
49
50