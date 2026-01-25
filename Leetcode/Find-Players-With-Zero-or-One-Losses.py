1class Solution:
2    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
3        # cleaner version
4        from collections import defaultdict
5        zero = []
6        one = []
7
8        losses = defaultdict(int)
9
10        for winner, loser in matches:
11            losses[winner] # zero exitst
12            losses[loser] += 1
13
14        for player, count in losses.items():
15            if count == 0: # not lost any match
16                zero.append(player)
17
18            if count == 1: # lost exactly one
19                one.append(player)
20
21
22        return [sorted(zero), sorted(one)]