1class Solution:
2    def convertDateToBinary(self, date: str) -> str:
3        l = 0
4        res = []
5
6        for r in range(len(date)):
7            if date[r] == "-":
8                s = date[l:r]
9                res.append(bin(int(s))[2:])
10                res.append("-")
11                l = r + 1
12        
13        ## last segment
14        res.append(bin(int(date[l:r+1]))[2:])
15
16        return "".join(res)
17