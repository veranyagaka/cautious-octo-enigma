1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        """ two pointers, sort, pick one no look for the other two using two pointers
4        """
5        nums.sort()
6        res = []
7
8        for i in range(len(nums)):
9            a = nums[i]
10            if a > 0: # all no are positive
11                break
12
13            if i > 0 and a == nums[i-1]: # skip duplicates
14                continue
15
16            l = i + 1
17            r = len(nums) - 1
18
19            while l < r:
20                threeSum = a + nums[l] + nums[r]
21                if threeSum > 0:
22                    r -= 1
23
24                elif threeSum < 0:
25                    l += 1
26
27                else: # threeSum == 0:
28                    res.append([a, nums[l], nums[r]])
29                    l += 1
30                    r -= 1
31
32                    while nums[l] == nums[l-1] and l < r:
33                        l += 1 # skip duplicates
34        return res