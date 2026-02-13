1class Solution:
2    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
3        m, n = len(image), len(image[0])
4        for i in range(m):
5            for j in range((n+1)//2): # go halfway
6                image[i][j], image[i][n-1-j] = 1 - image[i][n-1-j], 1 - image[i][j]
7
8        return image