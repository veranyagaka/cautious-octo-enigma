1class Solution:
2    def kthGrammar(self, n: int, k: int) -> int:
3        ## kidus
4        # base case
5        if n == 1:
6            return 0
7
8        total_no = 2 ** (n-1)
9        half = total_no // 2
10
11        if k > half: ## its in the right half
12            return 1 - self.kthGrammar(n, k-half)
13
14        else: ## its in the left half, just move up one row
15            return self.kthGrammar(n - 1, k)
16
17        """
18        observations
19        1. previous row is the next rows prefix
20        2. left half is negation of the right half
21        0
22        01
23        0110
24        01101001
25
26        use recursion
27        """
28        