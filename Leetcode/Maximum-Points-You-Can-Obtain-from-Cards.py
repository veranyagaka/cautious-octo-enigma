1class Solution:
2    def maxScore(self, cardPoints: List[int], k: int) -> int:
3        n = len(cardPoints)
4        score = sum(cardPoints[n-k:]) # taking last k cards
5
6        max_score = score
7
8        for i in range(k): 
9            score += cardPoints[i] - cardPoints[n-k+i] 
10
11            max_score = max(max_score, score)
12
13        return max_score
14
15        """
16        cardPoints = [100, 40, 17, 9, 73, 75]
17        k = 3
18        9 + 73 + 76
19
20        i = 0 
21        100 + 73 + 75
22
23        i = 1
24
25        100 + 40 + 75
26
27        i = 3
28        100 + 40 + 17
29        """