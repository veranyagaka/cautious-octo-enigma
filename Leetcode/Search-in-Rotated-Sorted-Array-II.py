1class Solution:
2    def search(self, nums: List[int], target: int) -> bool:
3        ## supposed to use binary search
4
5        ## supposed to look for the sorted half
6        low = 0
7        high = len(nums) -1
8
9        while low <= high:
10            mid = (low + high) // 2
11            curr = nums[mid]
12
13            if curr == target:
14                return True
15
16            ## reduce search space if we get duplicates
17            if nums[low] == curr == nums[high]:
18                low += 1
19                high -= 1
20                continue
21
22            ## look for the sorted half
23
24            if nums[low] <= curr: ## the left half is sorted
25                ## check if target lies here
26
27                if nums[low] <= target < curr: # ie try looking for 5 in the example
28                    high = mid - 1
29
30                else:
31                    low = mid + 1
32
33
34            else:
35                ## it was the right half which was sorted
36                if curr < target <= nums[high]: # try with 2
37                    low = mid + 1
38
39                else:
40                    high = mid - 1
41
42
43
44        """
45        walkthrough
46        nums = [2,5,6,0,0,1,2], target = 5
47        low = 0
48        high = 6
49        mid = 3 the num is 0
50
51
52
53
54        """
55
56
57        return False # the num was not found