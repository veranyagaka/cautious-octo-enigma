1class Solution:
2    def minOperations(self, nums: List[int], k: int) -> int:
3        
4        total = sum(nums)
5
6        return total % k
7
8        