1class Solution:
2    def singleNonDuplicate(self, nums: List[int]) -> int:
3
4        ##edge case
5        if len(nums) == 1:
6            return nums[0]
7        
8        low = 0
9        high = len(nums) - 1
10
11        while low < high:
12            mid = (low + high ) // 2
13
14            if mid % 2 == 0:
15
16                if nums[mid] == nums[mid + 1]:
17                    ## the single element is further right
18                    low = mid + 2
19
20                else:
21                    high = mid
22
23            ## is there really a condition fo us to use both/ check the left of the right       
24            else:
25                if nums[mid] == nums[mid - 1]:
26                    ## the single element is further right
27                    low = mid + 1
28
29                else:
30                    high = mid
31
32
33            ## we want to know which way to go look, left or right
34
35        return nums[low]
36        
37        """
38        dry run
39        [1,1,2,3,3,4,4,8,8] 
40        low = 0
41        high = 8
42        mid = 4
43
44        4 is even
45
46        [1,1,3,3,4,4,8,8, 9]
47
48
49
50
51        """