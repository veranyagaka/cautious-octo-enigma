1class Solution:
2    def maximumUniqueSubarray(self, nums: List[int]) -> int:
3
4        n = len(nums)
5        max_score = 0
6        score = 0
7        left = 0
8        seen = set()
9
10        for right in range(n):
11            while nums[right] in seen:
12                seen.remove(nums[left])
13                score -= nums[left]
14                left += 1
15            
16            score += nums[right]
17
18            seen.add(nums[right])
19
20            max_score = max(score, max_score)
21
22        return max_score
23
24        