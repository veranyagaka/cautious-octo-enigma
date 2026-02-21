1class Solution:
2    def countPairs(self, nums: List[int], k: int) -> int:
3        n = len(nums)
4        answer = 0
5        for i in range(n):
6            for j in range(i+1, n):
7                if nums[i] == nums[j] and ((i * j) % k) == 0 :
8                    answer += 1
9
10        return answer
11