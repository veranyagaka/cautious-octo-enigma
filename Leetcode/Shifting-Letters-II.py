1class Solution:
2    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
3        n = len(s)
4        prefix = [0] * n
5
6        for l, r, direction in shifts:
7            val = 1 if direction == 1 else -1
8
9            prefix[l] +=  val
10            if r + 1 < n:
11                prefix[r + 1] -=  val
12
13        for i in range(1, n):
14            prefix[i] += prefix[i-1]
15
16        result = []
17        for i in range(n):
18            original = ord(s[i]) - ord('a')
19            new_val = (original + prefix[i] ) % 26 #wrap
20            result.append(chr(new_val + ord('a')))
21
22        return "".join(result)