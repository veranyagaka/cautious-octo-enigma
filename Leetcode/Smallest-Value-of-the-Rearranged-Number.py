1class Solution:
2    def smallestNumber(self, num: int) -> int:
3        a = list(str(num))
4        res = []
5
6        ## negative
7        if a[0] == "-": 
8            res.append(a[0])
9            res.extend(sorted(a[1:], reverse=True))
10        
11
12        elif "0" in a: ## contains zero
13            a = sorted(a)
14            print(a)
15            for i, num in enumerate(a):
16                if num != "0":
17                    res.append(a[i])
18                    del a[i]
19                    break
20                    
21            res.extend(a)
22        
23        else:
24            res = sorted(a)
25
26        return int("".join(res))
27