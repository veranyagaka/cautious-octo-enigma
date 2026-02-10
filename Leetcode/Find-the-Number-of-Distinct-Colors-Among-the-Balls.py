1class Solution:
2    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
3        res = []
4        ball_color = {}
5        color_count = {}
6        distinct = 0
7
8        for x, y in queries:
9            if x in ball_color: # already has a color; remove
10                old = ball_color[x]
11                color_count[old] -= 1
12
13                if color_count[old] == 0:
14                    distinct -= 1
15                    del color_count[old]
16
17            if y not in color_count:
18                color_count[y] = 0
19
20                distinct += 1
21            color_count[y] += 1
22            
23            ball_color[x] = y
24            res.append(distinct)
25
26        return res
27