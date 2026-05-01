1class Solution:
2    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
3        ## sliding window
4
5        subs = 0
6        n = len(nums)
7        left = 0
8        product = 1
9
10
11        for right in range(n):
12            product *= nums[right]
13
14            while product >= k and left <= right:
15                product //= nums[left]
16                left += 1
17
18            subs += right - left + 1
19
20        return subs