1class Solution:
2    def numSpecial(self, mat: List[List[int]]) -> int:
3        m = len(mat)
4        n = len(mat[0])
5
6        res = 0
7
8        row_count = [0] *m
9        col_count = [0] * n
10
11        for i in range(m):
12            for j in range(n):
13                
14                if mat[i][j] == 1:
15                    row_count[i] += 1
16                    col_count[j] += 1
17    
18        for i in range(m):
19            for j in range(n):
20                
21                if mat[i][j] == 1 and row_count[i] == 1 and col_count[j] == 1:
22                    res += 1
23        return res  