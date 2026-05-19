1class Solution:
2    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
3        
4        ## the arrays are already sorted
5        ## two pointers approach
6        l = 0
7        r = 0
8        min_len = min(len(nums1), len(nums2))
9
10        while l < len(nums1) and r < len(nums2):
11            if nums1[l] == nums2[r]:
12                return nums1[l]
13
14            elif nums1[l] > nums2[r]:
15                r += 1
16
17            else:
18                l += 1
19
20        return -1