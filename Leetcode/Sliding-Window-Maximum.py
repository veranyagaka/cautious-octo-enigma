1class Solution:
2    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
3        ## neetcode help
4        ## using a mono decreasing queue
5        from collections import deque
6        res = []
7        l = r = 0
8        queue = deque()
9
10        while r < len(nums):
11            while queue and nums[queue[-1]] < nums[r]: 
12                queue.pop()
13
14            queue.append(r)
15
16            ## remove the lefr value if greater than window
17            if l > queue[0]:
18                queue.popleft()
19
20            if (r + 1) >= k:
21                res.append(nums[queue[0]])
22                l += 1
23
24            r += 1
25
26        return res