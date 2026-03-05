1class Solution:
2    def minOperations(self, s: str) -> int:
3
4        pattA, pattB = 0, 0
5        n = len(s)
6        str1 = [0] * n
7        for x in range(0, n - 1, 2):
8            str1[x] = 0
9            str1[x+1] = 1
10        
11        str2 = [1] * n
12        for x in range(0, n - 1, 2):
13            str2[x] = 1
14            str2[x+1] = 0
15
16        for i in range(n):
17        
18            if int(s[i]) != str1[i]:
19                pattA += 1
20
21        for i in range(n):
22            if int(s[i]) != str2[i]:
23                pattB += 1
24        # print(str1)
25        # print(str2)
26        
27        ans = min(pattA, pattB)
28        return ans
29
30        """
31        two patterns A and B; A: starts with 0 
32        and B starts with 1"""