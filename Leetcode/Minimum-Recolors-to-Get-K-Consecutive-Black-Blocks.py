1class Solution:
2    def minimumRecolors(self, blocks: str, k: int) -> int:
3        # k is the required no of black color
4        # could keep track of the count
5        l = 0
6        n = len(blocks)
7        first = blocks[:k]
8        res = first.count("W")
9        curr = res
10
11        for r in range(k, n):
12            if blocks[r] == "W":
13                curr += 1
14
15            if (r - l +1) > k and blocks[l] == "W":
16                curr -= 1
17            
18            l += 1
19
20            res = min(res, curr)
21        
22        return res