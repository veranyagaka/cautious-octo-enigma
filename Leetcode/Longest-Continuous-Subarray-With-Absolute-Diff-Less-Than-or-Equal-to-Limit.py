1class Solution:
2    def longestSubarray(self, nums: List[int], limit: int) -> int:
3        # neetcode help
4        # mono increasing and mon decreasing
5        min_q, max_q = deque(), deque()
6        res = 0
7        l = 0
8
9        for r in range(len(nums)):
10            while min_q and min_q[-1] > nums[r]:
11                min_q.pop()
12            
13            while max_q and max_q[-1] < nums[r]:
14                max_q.pop()
15
16            max_q.append(nums[r])
17            min_q.append(nums[r])
18
19            while abs(min_q[0] - max_q[0]) > limit:
20                if nums[l] == max_q[0]:
21                    max_q.popleft()
22                if nums[l] == min_q[0]:
23                    min_q.popleft()
24                l += 1
25            res = max(res, r - l +1)
26
27        return res