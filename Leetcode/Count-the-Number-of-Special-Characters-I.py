1class Solution:
2    def numberOfSpecialChars(self, word: str) -> int:
3        
4        search_space = "abcdefghijklmnopqrstuvwxyz"
5
6        count = 0
7
8        seen = set()
9
10        for ch in search_space:
11
12            if ch not in seen and ch in word and ch.upper() in word:
13                count += 1
14                
15            seen.add(ch)
16
17        # for ch in word:
18        #     ch = ch.lower()
19
20        #     if ch not in seen and ch in search_space and ch.upper() in search_space:
21        #         count += 1
22
23        #     seen.add(ch)
24
25        return count