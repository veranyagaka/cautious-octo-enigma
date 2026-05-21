1class Solution:
2    def isMonotonic(self, nums: List[int]) -> bool:
3        first = nums[0]
4        second = nums[-1]
5
6        increasing = True if first < second else False
7
8        
9        for i in range(len(nums) - 1):
10            if (nums[i] < nums[i + 1] and not increasing) or (nums[i] > nums[i + 1] and increasing):
11                # print(i)
12                return False
13 
14
15        return True