1class Solution:
2    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
3        m, n = len(mat), len(mat[0])
4        result = []
5
6        # group by diagonals
7        diagonals = collections.defaultdict(list)
8
9        for i in range(m):
10            for j in range(n):
11                diagonals[i+j].append(mat[i][j])
12
13        for k in range(m + n -1):
14            if k % 2 == 0:
15                result.extend(diagonals[k][::-1]) # reverse
16            
17            else:
18                result.extend(diagonals[k])
19
20
21        # order matters
22
23        # even - reverse, odd - keep
24
25
26        return result