1class Solution:
2    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
3        max_sum = 0
4        window_sum = 0
5        left = 0
6        window_count = collections.Counter()
7
8
9        for right in range(len(nums)):
10            window_count[nums[right]] += 1
11            window_sum += nums[right]
12
13            while (right - left + 1) > k or window_count[nums[right]] > 1:
14                window_count[nums[left]] -= 1
15                window_sum -= nums[left]
16
17                left += 1
18
19            if right - left + 1 == k:
20                max_sum = max(max_sum, window_sum)
21            
22
23        return max_sum