1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        """
4        Do not return anything, modify nums1 in-place instead.
5        """
6        # three pointers
7        x = m - 1 # valid nums1 pointer
8        y = n - 1 # nums2 pointer
9        z = m + n - 1 # very end nums1 pointer
10
11        # merging backwards
12        # for i in range(len(nums1), 0, -1):
13        while x >= 0 and y >= 0:
14            max_num = max(nums1[x], nums2[y])
15            nums1[z] = max_num
16
17            if nums2[y] > nums1[x]:
18                y -= 1
19
20            else:
21                x -= 1
22
23            z -= 1
24
25        while y >= 0:
26            nums1[z] = nums2[y]
27            y -= 1
28            z -= 1
29
30        