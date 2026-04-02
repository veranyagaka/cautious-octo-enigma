1class Solution:
2    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
3
4        intersections = []
5        l, r = 0, 0
6
7        while l < len(firstList) and r < len(secondList):
8            start = max(firstList[l][0], secondList[r][0])
9            end = min(firstList[l][1], secondList[r][1])
10
11            if start <= end: # valid intersection
12                intersections.append([start, end])
13
14            # move pointers
15            if (firstList[l][1] < secondList[r][1]):
16                l += 1
17
18            else:
19                r += 1
20
21            
22
23        return intersections
24        