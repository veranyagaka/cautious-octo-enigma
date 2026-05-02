1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        
4        left = 0
5        right = len(nums) - 1
6
7        while left <= right:
8            mid = (left + right) // 2
9
10            if target == nums[mid]:
11                return mid
12
13            ## look for which half is sorted based on mid, left and right
14            if nums[left] <= nums[mid]:
15                # the left half is sorted
16                if nums[left] <= target < nums[mid]: # is the target in the sorted half?
17                    right = mid - 1
18                else:
19                    left = mid + 1
20
21            else:
22                ## the right half is the sorted one
23                # check if target is in the right sorted hald
24
25                if nums[mid] < target <= nums[right]:
26                    left = mid + 1
27                else:
28                    right = mid - 1
29
30
31        return -1 ## did not find