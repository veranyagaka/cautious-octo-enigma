1class Solution:
2    def minWindow(self, s: str, t: str) -> str:
3        # neetcode help
4        
5        if t == "": return "" # edge case
6
7        countT, window = {}, {}
8
9        for c in t:
10            countT[c] = 1 + countT.get(c, 0)
11
12        have, need = 0, len(countT)
13        res, resLen = [-1, -1], float("infinity")
14
15        l = 0
16
17        for r in range(len(s)):
18            c = s[r]
19            window[c] = 1 + window.get(c, 0)
20
21            if c in countT and window[c] == countT[c]:
22                have += 1
23
24            while have == need: # we need minimum 
25                
26                if (r-l+1) < resLen:
27                    res = [l, r]
28                    resLen = (r-l+1)
29
30                window[s[l]] -= 1
31
32                if s[l] in countT and window[s[l]] < countT[s[l]]:
33                    have -= 1
34
35                l += 1 # keep decreasing the window
36
37        l, r = res
38
39        return s[l:r+1] if resLen != float("infinity") else ""