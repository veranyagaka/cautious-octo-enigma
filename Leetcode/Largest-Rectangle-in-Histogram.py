1class Solution:
2    def largestRectangleArea(self, heights: List[int]) -> int:
3        n = len(heights)
4        PSE = [-1] * n
5        NSE = [n] * n
6
7        stack = []
8        # PSE
9        for i in range(n):
10            while stack and heights[stack[-1]] >= heights[i]:
11                stack.pop()
12            # fill values
13            PSE[i] = stack[-1] if stack else -1
14            stack.append(i)
15
16
17        stack = []
18        # NSE
19        for i in range(n-1, -1, -1): # reverse order
20            while stack and heights[stack[-1]] >= heights[i]:
21                stack.pop()
22            # fill values
23            NSE[i] = stack[-1] if stack else n
24            stack.append(i)
25            
26        max_area = 0
27
28        for i in range(n):
29            width = NSE[i] - PSE[i] - 1
30            max_area = max(max_area, heights[i] * width)
31
32        return max_area
33
34        """
35        a2sv kidus
36        monostack; increasing monotonic stack
37        the stack is storing the index
38        pse and nse
39        """
40
41