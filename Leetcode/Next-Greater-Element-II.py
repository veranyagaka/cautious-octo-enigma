1class Solution:
2    def nextGreaterElements(self, nums: List[int]) -> List[int]:
3        stack = []
4        n = len(nums)
5
6        ans = [-1] * n
7        ## loop twice in the array
8
9        for i in range(n*2):
10
11            while stack and nums[stack[-1]] < nums[i%n]:
12                idx = stack.pop()
13                ans[idx] = nums[i%n]
14            if i < n:
15                stack.append(i)
16
17        return ans
18
19        """
20        what is stack storing:
21        the index
22        curcular array: use modulos symbol
23        """