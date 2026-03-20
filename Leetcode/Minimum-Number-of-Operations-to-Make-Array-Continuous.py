1class Solution:
2    def minOperations(self, nums: List[int]) -> int:
3        # neetcode help
4        nums.sort()
5        n = len(nums)
6
7        nums = sorted(set(nums))
8        ops = n
9
10        right = 0
11
12        for left in range(len(nums)):
13
14            while right < len(nums) and nums[right] < nums[left] + n:
15                right += 1
16
17            window = right - left # no + 1 because its inclusive
18
19            ops = min(ops, n - window)
20
21
22        return ops
23
24        # l = 0
25        # r = n - 1
26
27        # while l < r:
28        #     if nums[r] - nums[1] != n -1: 
29        #         ops += 1
30
31        #     if nums[l] == nums[r]: # finding duplicates have to replace
32        #         ops += 1
33
34        #     l += 1
35        #     r -= 1
36
37        # return ops
38        
39
40        """things to check
41        - all no are unique
42        and max-min == n -1"""