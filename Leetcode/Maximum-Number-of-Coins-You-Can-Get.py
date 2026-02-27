1class Solution:
2    def maxCoins(self, piles: List[int]) -> int:
3        """ NICOLE
4        sort
5        then cut the first i/3 which will go to bob
6        then loop every 2 elements and add it on
7        """
8        piles.sort()
9        n = len(piles)
10        t = n // 3
11        answer = 0
12
13        for i in range(t, n, 2):
14            answer += piles[i]
15
16        return answer
17