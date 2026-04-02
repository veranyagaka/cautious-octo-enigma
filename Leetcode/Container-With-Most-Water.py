1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        n = len(height)
4        max_amount = 0
5        l = 0
6        r = n -1
7
8        while l < r:
9            area = min(height[l], height[r]) * (r - l)
10
11            if height[l] < height[r]: # looking for a taller line
12                l += 1
13
14            else:
15                r -= 1
16
17            max_amount = max(area, max_amount)
18        return max_amount