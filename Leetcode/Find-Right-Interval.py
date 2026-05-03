1class Solution:
2    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
3        ## using heaps
4        # some guy from yt
5
6        starts, ends, output = [], [], []
7
8        for i, (st, en) in enumerate(intervals):
9            heapq.heappush(ends, (en, i))
10            heapq.heappush(starts, (st, i))
11
12        heapq.heappush(starts, (float('inf'), -1))
13
14        start = float('-inf')
15
16        while ends:
17            end, i_end = heapq.heappop(ends)
18
19            while starts and start < end:
20                start, i_start = heapq.heappop(starts)
21
22                if start >= end: break
23
24            output.append((i_end, i_start))
25
26
27        return [i2 for i1, i2 in sorted(output)]
28
29
30        # n = len(intervals)
31        # res = [-1] * n
32
33        # for start, end in intervals:
34
35
36        # return res