1class Solution:
2    def majorityElement(self, nums: List[int]) -> List[int]:
3        from collections import Counter
4        n = len(nums)
5        res = []
6        count = Counter(nums)
7        for i in nums:
8            if count[i] > int(n/3) and i not in res:
9                res.append(i)
10        return res
11        