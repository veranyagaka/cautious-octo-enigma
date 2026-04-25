1class Solution:
2    def countElements(self, nums: List[int]) -> int:
3        
4        """ we can first sort 
5        then coudn the no from second indext to last index 
6        and just do some checks
7                return len(nums[1:n-1])
8        """
9        # nums = [11,7,2,15]
10        nums.sort()
11        min_no = nums[0]
12        max_no = nums[-1]
13        count = 0
14
15        for n in nums:
16            # print(min_no, n, max_no)
17            # print("---")
18            if min_no < n < max_no:
19                count += 1 
20
21        return count
22