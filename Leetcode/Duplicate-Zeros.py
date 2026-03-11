1class Solution:
2    def duplicateZeros(self, arr: List[int]) -> None:
3        """
4        Do not return anything, modify arr in-place instead.
5        """
6        #get the no of zeros
7        # shiftin from right to leleft
8        # two pointers
9        no_of_zero = arr.count(0)
10        n = len(arr)
11        i = n - 1
12        j = n + no_of_zero - 1
13
14        while i < j:
15            if j < n:
16                arr[j] = arr[i]
17
18            if arr[i] == 0:
19                j -= 1
20
21                if j < n:
22                    arr[j] = 0
23
24
25            i -= 1
26            j -= 1