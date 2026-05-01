1class Solution:
2    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
3        ### note it is sorted
4        ## neetcode help
5        ## using binary search
6        ## using the window size themselves
7        l = 0
8        r = len(arr) - k
9
10        while l < r:
11            mid = (l + r )// 2
12            ## m is the beginning of the window
13            if x - arr[mid] > arr[mid+k] - x: ## just outside the window
14                l = mid + 1
15
16            else:
17                r = mid
18
19
20        return arr[l:l+k]