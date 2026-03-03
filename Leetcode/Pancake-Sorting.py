1class Solution:
2    def pancakeSort(self, arr: List[int]) -> List[int]:
3        res = []
4        n = len(arr)
5
6        def reverse_subarry(arr, start, end):
7            while start < end:
8                arr[start], arr[end] = arr[end], arr[start]
9                start += 1
10                end -=1
11
12            return arr
13
14        def find_max(arr, l, r):
15            maxim = l
16            for i in range(l+1, r):
17                if arr[i] > arr[maxim]:
18                    maxim = i
19
20            return maxim
21
22
23        for i in range(n, 1, -1):
24            max_index = find_max(arr, 0, i)            
25            arr = reverse_subarry(arr, 0, max_index)
26            res.append(max_index+1)
27            arr = reverse_subarry(arr, 0, i-1)
28            res.append(i)
29
30        return res
31
32
33
34"""
35sorting from the last to the first
36therefore take the big element take it to the front and do the flip"""