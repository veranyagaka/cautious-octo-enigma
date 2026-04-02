1class Solution:
2    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
3        max_sum = 0
4        window_sum = 0
5        left = 0
6        seen = set()
7
8
9        for right in range(len(nums)):
10            while nums[right] in seen:
11                seen.remove(nums[left])
12                window_sum -= nums[left]
13                left += 1
14
15            window_sum += nums[right]
16
17            while (right - left + 1) > k :
18                seen.remove(nums[left])
19                window_sum -= nums[left]
20
21                left += 1
22
23            seen.add(nums[right])
24
25            if right - left + 1 == k:
26                max_sum = max(max_sum, window_sum)
27            
28        return max_sum