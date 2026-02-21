matrix = []
for _ in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)
n = len(matrix)
center = n // 2
steps = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            steps = abs(i - center) + abs(j - center)

print(steps)
"""
0 0 0 0 0
0 0 0 0 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
"""