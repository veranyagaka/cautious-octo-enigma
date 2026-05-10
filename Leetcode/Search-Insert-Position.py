1class Solution:
2    def searchInsert(self, nums: List[int], target: int) -> int:
3        
4        ## it is sorted
5        ## use binary searfch
6
7        low = 0
8        high = len(nums) -1
9
10        while low <= high:
11            mid = (low + high) //2
12
13            if nums[mid] == target:
14                return mid
15
16            elif nums[mid] > target:
17                ## search in the left half then
18                high = mid - 1
19
20            else:
21                low = mid + 1
22
23
24        return low