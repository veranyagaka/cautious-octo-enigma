1class Solution:
2    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
3        
4        ## brute force
5        ## merge and sort
6        total = nums1 + nums2
7        total.sort()
8        n = len(total)
9
10        if n % 2 == 1:
11            return total[n // 2]
12
13        else:
14            return (total[n // 2] + total[(n // 2) - 1])  / 2
15       
16
17        