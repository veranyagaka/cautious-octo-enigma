1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4
5        prefix = [1] * (n+1)
6        for i, num in enumerate(nums):
7            prefix[i+1] = nums[i] * prefix[i]
8
9        suffix = [1] * (n+1)
10        for i in range(n-1 ,-1, -1):
11            suffix[i] = suffix[i+1] * nums[i]
12
13        answer = [0] * n
14        for i in range(n):
15            answer[i] = prefix[i] * suffix[i+1]
16
17        return answer