1class Solution:
2    def rotate(self, matrix: List[List[int]]) -> None:
3        """
4        Do not return anything, modify matrix in-place instead.
5        """
6        # transpose and reverse
7        n = len(matrix)
8
9        for i in range(n):
10            for j in range(i+1, n): # swap half the matrix
11                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
12
13
14        for row in matrix:
15            row.reverse()