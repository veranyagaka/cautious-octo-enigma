1class Solution:
2    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
3        m, n = len(matrix), len(matrix[0])
4
5        top, bottom = 0, m -1
6        left, right = 0, n -1
7
8        res = []
9
10        while top <= bottom and left <= right:
11            for x in range(left, right +1):
12                res.append(matrix[top][x])
13            top += 1
14
15            for x in range(top, bottom + 1):
16                res.append(matrix[x][right])
17            
18            right -= 1
19            if top <= bottom:
20                
21                for x in range(right, left - 1, -1):
22                    res.append(matrix[bottom][x])
23                bottom -= 1
24
25            if left <= right:
26                for x in range(bottom, top - 1, -1):
27                    res.append(matrix[x][left])
28                
29                left += 1
30
31
32        return res
33
34