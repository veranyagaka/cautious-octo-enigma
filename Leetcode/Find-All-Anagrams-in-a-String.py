1class Solution:
2    def findAnagrams(self, s: str, p: str) -> List[int]:
3        n = len(s)
4        res = []
5        window = Counter()
6        k = len(p)
7
8
9        ## frequency counts
10        p_count = collections.Counter(p)
11        for i in range(n):
12            window[s[i]] += 1
13
14            if i >= k: # window exceeds size remove the left most element
15                if window[s[i-k]] == 1: # the character leaving the window
16                    del window[s[i-k]] # deleting the key entirely
17
18                else:
19                    window[s[i-k]] -= 1
20                    
21
22
23            if window == p_count:
24                res.append(i-k+1)
25        
26
27        return res
28