1class Solution:
2    def buildArray(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4        ans = [0] * n
5        for i in range(n):
6            ans[i] = nums[nums[i]]
7
8        return ans
9        