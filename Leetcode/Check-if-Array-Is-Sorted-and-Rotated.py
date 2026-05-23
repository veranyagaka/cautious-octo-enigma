1class Solution:
2    def check(self, nums: List[int]) -> bool:
3
4        """
5        we are only allowing one count
6
7        3 4 5 1 2
8
9        2 1 3 4
10        """
11        
12        n = len(nums)
13        count = 0
14
15        for i in range(n - 1):
16            if nums[i] > nums[i+1]:
17                count += 1
18        # print(count)
19        if count == 0:
20            return True
21
22        if count == 1 and (nums[0] >= nums[-1]):
23            """
24            the arr has been rotated once so that means the first element must be greater than the last element
25            """
26            return True
27        return False