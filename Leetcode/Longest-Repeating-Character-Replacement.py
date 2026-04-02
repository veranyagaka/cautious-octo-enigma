1class Solution:
2    def characterReplacement(self, s: str, k: int) -> int:
3        ## sliding window and frequency counting
4        n = len(s)
5
6        left = 0
7
8        window = Counter()
9
10        max_length = 0
11        max_freq = 0
12
13        for right in range(n):
14            window[s[right]] += 1
15
16            max_freq = max(max_freq, window[s[right]])
17
18            if (right - left + 1) - max_freq > k:
19                window[s[left]] -= 1
20
21                left += 1
22
23            curr_length = right - left + 1
24            max_length = max(max_length, curr_length)
25
26
27        return max_length