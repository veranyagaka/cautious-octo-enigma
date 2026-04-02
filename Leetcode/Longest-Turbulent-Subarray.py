1class Solution:
2    def maxTurbulenceSize(self, arr: List[int]) -> int:
3        """
4        neetcode help
5        need to keep track of the previous sign
6        sliding window
7        """
8
9        res = 1
10        l, r = 0, 1
11        prev = ""
12        
13
14        while r < len(arr):
15            if arr[r-1] > arr[r] and prev != ">":
16                res = max(res, r - l + 1)
17                r += 1
18                prev = ">"
19
20            elif arr[r-1] < arr[r] and prev != "<":
21                res = max(res, r - l + 1)
22                r += 1
23                prev = "<"
24
25            else: # we have an equal sign or we done have a turbulence anymore, move the left
26                if arr[r-1] == arr[r]:
27                    r = r + 1
28
29                l = r - 1
30                prev = "" # show that we are starting again
31
32        return res
33