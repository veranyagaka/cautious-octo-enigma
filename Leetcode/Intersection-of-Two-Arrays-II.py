1class Solution:
2    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
3        res = []
4        l = 0
5        r = 0
6
7        nums1.sort()
8        nums2.sort()
9
10
11        while r < len(nums2) and l < len(nums1):
12
13            if nums1[l] == nums2[r]:
14                
15                res.append(nums2[r])
16                l += 1
17                r += 1
18
19            elif nums1[l] > nums2[r]:
20                r += 1
21
22            elif nums1[l] < nums2[r]:
23                l += 1
24
25            
26
27        return res