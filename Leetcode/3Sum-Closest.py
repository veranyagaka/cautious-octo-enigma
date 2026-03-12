1class Solution:
2    def threeSumClosest(self, nums: List[int], target: int) -> int:
3        
4
5        """how to do closest?"""
6        nums.sort()
7        closest_sum = float('inf')
8
9        for i in range(len(nums)):
10            a = nums[i]
11            l = i + 1
12            r = len(nums) - 1
13
14            while l < r:
15                curr_sum = a + nums[l] + nums[r]
16
17                if abs(curr_sum - target) < abs(closest_sum - target):
18                    closest_sum = curr_sum
19                
20                if curr_sum == target:
21                    return curr_sum
22
23                elif curr_sum < target:
24                    l += 1
25
26                else:
27                    r -= 1
28
29        return closest_sum