1class Solution:
2    def maxVowels(self, s: str, k: int) -> int:
3        vowels = {"a", "e", "i", "o", "u"}
4        
5        n = len(s)
6        #first_count = sum(ch in vowels for ch in s[:k])
7        max_count = 0
8        left = 0
9        curr_count = 0
10
11        for right in range(n):
12            if s[right] in vowels:
13                curr_count += 1
14
15            while (right - left + 1) > k:
16                if s[left] in vowels:
17                    curr_count -= 1
18                left += 1
19                
20            max_count = max(max_count, curr_count)
21
22        return max_count