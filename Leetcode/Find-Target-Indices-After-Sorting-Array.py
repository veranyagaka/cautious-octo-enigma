1class Solution:
2    def targetIndices(self, nums: List[int], target: int) -> List[int]:
3        nums.sort()
4        res = []
5
6        for i, num in enumerate(nums):
7            if num == target:
8                res.append(i)
9
10        return res
11