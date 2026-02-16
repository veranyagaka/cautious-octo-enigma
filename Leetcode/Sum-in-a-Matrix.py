1class Solution:
2    def matrixSum(self, nums: List[List[int]]) -> int:
3        score = 0
4        m, n = len(nums), len(nums[0])
5        for i in range(n):
6            col = []
7            for row in nums:
8                
9                max_no = max(row)
10                col.append(max_no)
11                row.remove(max_no)
12                #print(max_no)
13            score += max(col)
14
15        return score
16