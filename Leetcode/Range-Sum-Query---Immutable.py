1class NumArray:
2
3    def __init__(self, nums: List[int]):
4        self.prefix = [0] * (len(nums)+1)
5
6        for i  in range(len(nums)):
7            self.prefix[i+1] = self.prefix[i] + nums[i]
8
9        
10
11    def sumRange(self, left: int, right: int) -> int:
12        return self.prefix[right+1] - self.prefix[left]
13
14        
15
16
17# Your NumArray object will be instantiated and called as such:
18# obj = NumArray(nums)
19# param_1 = obj.sumRange(left,right)