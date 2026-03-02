1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        intervals.sort(key = lambda x: x[0])
4        merged = [intervals[0]]
5
6        for curr in intervals[1:]:
7            prev = merged[-1] # get the last thing merged: not copy a reference to the list
8
9            if curr[0] <= prev[1]: # overlap!
10                prev[1] = max(curr[1], prev[1])
11            else:
12                merged.append(curr)
13
14
15        return merged