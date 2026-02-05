1class Solution:
2    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
3        output = []
4        for i in range(len(nums)):
5            count = 0
6            for j in range(len(nums)):
7                if nums[j] < nums[i] and j != i:
8                    count += 1
9
10            output.append(count)
11
12
13        return output