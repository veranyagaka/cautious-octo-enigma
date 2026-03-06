1class Solution:
2    def findRelativeRanks(self, score: List[int]) -> List[str]:
3        
4        n = len(score)
5        res = []
6        ans = [""] * n
7        for i, num in enumerate(score):
8            res.append((num, i))
9        res.sort(reverse=True)
10
11        for rank, (num, index) in enumerate(res):
12            if rank == 0:
13                ans[index] = "Gold Medal"
14            elif rank == 1:
15                ans[index] = "Silver Medal"
16            elif rank == 2:
17                ans[index] = "Bronze Medal"
18            else:
19                ans[index] = str(rank + 1)
20        
21        return ans
22        # tf