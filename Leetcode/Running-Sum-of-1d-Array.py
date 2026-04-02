1class Solution:
2    def runningSum(self, nums: List[int]) -> List[int]:
3        res = []
4        running_sum = 0
5        for num in nums:
6            running_sum += num
7            res.append(running_sum)
8
9        return res