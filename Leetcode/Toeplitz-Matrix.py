1class Solution:
2    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
3        # compare with top left negihbour
4        m = len(matrix)
5        n = len(matrix[0])
6
7        for i in range(1, m):
8            for j in range(1, n):
9                if matrix[i][j] != matrix[i-1][j-1]:
10                    return False
11
12        return True
13
14