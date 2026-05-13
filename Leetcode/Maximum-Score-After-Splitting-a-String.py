1class Solution:
2    def maxScore(self, s: str) -> int:
3        
4        ## optimal use prefix sum
5
6        max_score = 0
7        ones_so_far = 0
8        total_ones = s.count("1")
9
10        for i in range(len(s) - 1):
11            if s[i] == '1':
12                ones_so_far += 1
13
14            left_zeros = (i + 1) - ones_so_far
15            right_ones = total_ones - ones_so_far
16
17            score = left_zeros + right_ones
18
19            max_score = max(max_score, score)
20
21
22        return max_score