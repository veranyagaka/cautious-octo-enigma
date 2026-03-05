1class Solution:
2    def frequencySort(self, s: str) -> str:
3        from collections import Counter
4        count = Counter(s)
5        # count.sort()
6        print(count)
7        res = []
8        sorted_counts = sorted(count.items(), key=lambda x: x[1], reverse=True)
9
10        for ch, times in sorted_counts:
11            
12            res.extend([ch for _ in range(times)])
13            
14        return "".join(res)