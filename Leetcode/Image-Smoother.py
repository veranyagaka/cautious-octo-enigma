1class Solution:
2    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
3        m, n = len(img), len(img[0])
4
5        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
6
7        result = [[0] * n for _ in range(m)]
8
9        for i in range(m):
10            for j in range(n):
11                total_sum = img[i][j]
12                count = 1
13
14                for dx, dy in directions:
15                    x = dx + i
16                    y = dy + j
17
18                    if 0 <= x < m and 0 <= y < n:
19                        total_sum += img[x][y]
20                        count += 1
21
22                result[i][j] = total_sum // count
23
24        return result
25