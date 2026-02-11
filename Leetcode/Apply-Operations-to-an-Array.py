1class Solution:
2    def applyOperations(self, nums: List[int]) -> List[int]:
3        res = []
4        
5        for i in range(len(nums)-1):
6            if nums[i] == nums[i+1]:
7                nums[i] *= 2
8                nums[i+1] = 0
9            
10        for num in nums:
11            if num != 0:
12                res.append(num)
13        no = nums.count(0)
14        res.extend([0] * no)
15
16        return res