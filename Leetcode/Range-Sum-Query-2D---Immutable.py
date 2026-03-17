1class NumMatrix:
2
3    def __init__(self, matrix: List[List[int]]):
4        m = len(matrix)
5        n = len(matrix[0])
6
7        self.prefix = [[0] * (n+1) for _ in range(m+1)]
8
9        for i in range(m):
10            for j in range(n):
11                # avoiding double counting
12                self.prefix[i+1][j+1] = ( 
13                    matrix[i][j]
14                    + self.prefix[i+1][j]
15                    + self.prefix[i][j+1]
16                    - self.prefix[i][j]
17                )
18
19    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
20        return (
21            self.prefix[row2+1][col2+1]
22            - self.prefix[row1][col2+1]
23            - self.prefix[row2+1][col1]
24            +self.prefix[row1][col1]
25
26        )
27
28
29
30# Your NumMatrix object will be instantiated and called as such:
31# obj = NumMatrix(matrix)
32# param_1 = obj.sumRegion(row1,col1,row2,col2)