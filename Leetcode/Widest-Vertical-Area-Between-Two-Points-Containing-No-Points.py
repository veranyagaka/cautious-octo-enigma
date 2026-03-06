1class Solution:
2    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
3        x_vals = []
4
5        for x, y in points:
6            x_vals.append(x)
7
8        x_vals = sorted(list(set(x_vals)))
9        max_val = 0
10        
11        for i in range(len(x_vals)-1):
12            curr_max = x_vals[i+1] - x_vals[i] 
13            max_val = max(curr_max, max_val)
14
15        return max_val