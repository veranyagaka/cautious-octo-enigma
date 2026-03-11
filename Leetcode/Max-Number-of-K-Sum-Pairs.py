1class Solution:
2    def maxOperations(self, nums: List[int], k: int) -> int:
3        
4        nums.sort()
5        ops = 0
6        left = 0
7        right = len(nums) - 1
8
9        while left < right:
10            if nums[left] + nums[right] == k:
11                ops += 1
12                left += 1
13                right -= 1
14
15            elif nums[left] + nums[right] < k: # skip the no there is nno possibility
16                left += 1
17
18            else:
19                right -= 1
20
21        return ops
22
23
24        """sort then 
25        left, right pointers
26
27        """