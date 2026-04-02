1class Solution:
2    def checkInclusion(self, s1: str, s2: str) -> bool:
3        # permutaion - basically count are the same
4
5        n = len(s1)
6        count_s1 = collections.Counter(s1)
7        window = collections.Counter()
8
9        left = 0
10
11        for right in range(len(s2)):
12            # if count
13            window[s2[right]] += 1
14
15            while (right-left + 1) > n:
16                window[s2[left]] -= 1
17
18                if window[s2[left]] == 0:
19                    del window[s2[left]]
20
21                left += 1
22            
23
24            if count_s1 == window:
25                return True
26
27        return False