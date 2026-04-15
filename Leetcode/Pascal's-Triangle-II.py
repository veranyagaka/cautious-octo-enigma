1class Solution:
2    def getRow(self, rowIndex: int) -> List[int]:
3        triangle = []
4        for i in range(rowIndex+1):
5            row = [1] * (i+1)
6
7            for j in range(1, i):
8                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
9
10            triangle.append(row)
11
12        return triangle[rowIndex]