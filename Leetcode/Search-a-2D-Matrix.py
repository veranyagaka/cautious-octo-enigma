1class Solution:
2    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
3        ## binary search
4
5        ## we just half the search space
6        m, n = len(matrix), len(matrix[0])
7
8        l = 0
9        r = m * n - 1
10
11        while l <= r:
12            mid = (l + r) // 2
13
14            row = mid // n
15            col = mid % n
16
17            val = matrix[row][col]
18
19            if val == target:
20                return True
21
22            elif val > target:
23                r = mid - 1
24
25
26            else:
27                l = mid + 1
28
29        return False
30