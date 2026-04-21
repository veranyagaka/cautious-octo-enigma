1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        n = len(nums)
4        low, high = 0, n - 1
5
6        while low <= high:
7            mid = (low + high) // 2
8
9            if nums[mid] == target:
10                return mid
11
12            elif nums[mid] < target:
13                low = mid + 1
14            
15            else:
16                high = mid - 1
17        
18        return -1
19