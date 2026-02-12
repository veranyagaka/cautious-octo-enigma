1class Solution:
2    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
3        total = 0
4
5        for i in points:
6
7            distance_count = {}
8            for j in points:
9                if i == j: # skip same points
10                    continue
11
12                dx = i[0] - j[0]
13                dy = i[1] - j[1]
14
15                dist = dx*dx + dy*dy
16                distance_count[dist] = distance_count.get(dist, 0) + 1
17
18            for m in distance_count.values():
19                total += m * (m - 1)
20
21
22        return total