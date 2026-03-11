1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        left = 0
4        max_length = 0
5        char_set = set()
6        n = len(s)
7
8        for right in range(n):
9            while s[right] in char_set:
10                char_set.remove(s[left])
11                left += 1
12
13            char_set.add(s[right])
14            window_length = right - left + 1
15            max_length = max(max_length, window_length)
16
17
18        return max_length