1class Solution:
2    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
3        nice = 0
4        n = len(nums)
5
6        for i in range(n):
7            if nums[i] % 2 == 0:
8                nums[i] = 0
9
10            else:
11                nums[i] = 1
12        
13        prefix = 0
14
15        count = {0:1}
16
17        for num in nums:
18            prefix += num # no of odd no we have seen so far
19
20            if prefix - k in count:
21                nice += count[prefix-k]
22
23
24            count[prefix] = count.get(prefix, 0) + 1
25        
26        return nice