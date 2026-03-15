1class Solution:
2    def countVowelSubstrings(self, word: str) -> int:
3        count = 0
4        n = len(word)
5        vowels = {"a", "e", "i", "o", "u"}
6        
7
8        for left in range(n):
9            seen = set()
10            
11            for right in range(left, n):
12                if word[right] not in vowels:
13                    break
14            
15                seen.add(word[right])
16
17                if len(seen) == 5:
18                    count += 1               
19
20        return count