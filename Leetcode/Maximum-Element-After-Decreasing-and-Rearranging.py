1class Solution:
2    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
3        arr.sort()
4        n = len(arr)
5        arr[0] = 1
6
7        for i in range(1, n):
8            if abs(arr[i] - arr[i-1]) > 1:
9                arr[i] = arr[i-1] + 1
10
11        return max(arr)