1class Solution:
2    def findPeakElement(self, nums: List[int]) -> int:
3
4        ## supposed to do binary search 
5        low, high = 0, len(nums) - 1
6
7        while low < high:
8            mid = (low + high) // 2
9            if nums[mid] > nums[mid+1]:
10                high = mid
11
12            else:
13                low = mid + 1
14
15        return low
16
17        """
18        looking if 
19        [5] > 4:
20        therefore we look to the left
21
22        [3] >[4]
23        low will now point to 4
24        """
25