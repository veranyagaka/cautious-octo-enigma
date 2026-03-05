1class Solution:
2    def minOperations(self, s: str) -> int:
3
4        patA, patB = 0, 0
5        expectedA, expectedB = "0", "1"
6
7        for c in s:
8            if c != expectedA:
9                patA += 1
10
11            if c != expectedB:
12                patB += 1
13
14            expectedA = "1" if expectedA == "0" else "0"
15            expectedB = "0" if expectedB == "1" else "1"
16
17        return min(patA, patB)
18
19        """
20        two patterns A and B; A: starts with 0 
21        and B starts with 1"""