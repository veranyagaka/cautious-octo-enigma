1class Solution:
2    def leftRightDifference(self, nums: List[int]) -> List[int]:
3        
4        answer = []
5        total = sum(nums)
6        leftSum = 0
7
8        for x in nums:
9            total -= x # right
10            answer.append(abs(total - leftSum))
11            leftSum += x
12
13
14        return answer