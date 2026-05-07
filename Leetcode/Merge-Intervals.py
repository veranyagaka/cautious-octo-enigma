1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        
4        ## first sort by the first no
5        intervals = sorted(intervals, key=lambda x: x[0])
6
7        res = [intervals[0]]
8
9        for i in intervals[1:]:
10            prev = res[-1]
11
12            if prev[1] >= i[0]: # we need to merge
13                prev[1] = max(i[1], prev[1])
14
15            else:
16                res.append(i)
17
18        return res