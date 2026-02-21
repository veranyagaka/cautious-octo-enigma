1class Solution:
2    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
3        m, n = len(matrix), len(matrix[0])
4        result = [[1] * m for _ in range(n)]
5
6        for i in range(m):
7            for j in range(n):
8                result[j][i] = matrix[i][j]
9
10        return result