1class Solution:
2    def countPairs(self, nums: List[int], target: int) -> int:
3        pairs = 0
4        n = len(nums)
5        nums.sort()
6
7        for i in range(n):
8            for j in range(i+1, n):
9                if nums[i] + nums[j] < target and i < j:
10                    pairs += 1
11
12                else:
13                    break
14
15
16        # i = 0
17        # j = 1
18
19        # while j < n:
20        #     if nums[i] + nums[j] < target:
21        #         pairs += 1
22
23        #     i += 2
24        #     j += 2
25
26        return pairs
27
28        """
29        """