1class NumArray:
2
3    def __init__(self, nums: List[int]):
4        self.nums = nums
5        
6
7    def sumRange(self, left: int, right: int) -> int:
8        running_sum = 0
9        while left <= right:
10            running_sum += self.nums[left]
11            left += 1
12
13
14        return running_sum
15
16        
17
18
19# Your NumArray object will be instantiated and called as such:
20# obj = NumArray(nums)
21# param_1 = obj.sumRange(left,right)