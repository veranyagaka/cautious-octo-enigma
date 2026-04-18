1class Solution:
2    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
3        ## neetcode help
4        ## if they intersect take the small speed
5
6        pairs = [[p, s] for p, s in zip(position, speed)]
7        pairs.sort(reverse=True)
8        stack = []
9
10        for p, s in pairs:
11            stack.append((target - p) / s)
12
13            if len(stack) >= 2 and stack[-1] <= stack[-2]:
14                stack.pop()
15
16        return len(stack)