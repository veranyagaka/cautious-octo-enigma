1class Solution:
2    def maxScore(self, s: str) -> int:
3        # precomputer a prefix sum of ones
4        n = len(s)
5        prefix = []
6        run_sum = 0
7        max_score = 0
8        count_zeros = 0
9
10        for i in range(n):
11            run_sum += int(s[i])
12            prefix.append(run_sum)
13
14        # l - r counting no of zeros
15        total_ones = prefix [-1]
16
17        for r in range(n-1):
18            ones_right = total_ones - prefix[r]
19
20            if s[r] == "0":
21                count_zeros += 1
22
23            curr_score = count_zeros + ones_right
24
25            max_score = max(max_score, curr_score)
26
27        return max_score