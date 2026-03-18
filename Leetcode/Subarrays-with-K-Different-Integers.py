1class Solution:
2    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
3        # neetcode help
4        # missing some valid subarrays:
5        # sliding window with 3 pointers
6
7        ans = 0
8        count = defaultdict(int)
9        l_near, l_far = 0, 0
10
11        for r in range(len(nums)):
12            num = nums[r]
13            count[num] += 1
14
15            # two scenarios to move our pointers
16            ## when we exceed the no of k
17            while len(count) > k:
18                count[nums[l_near]] -= 1
19                
20                if count[nums[l_near]] == 0:
21                    count.pop(nums[l_near])
22
23                l_near += 1
24                l_far = l_near
25
26            # when we have more no than needed, you can move near
27            while count[nums[l_near]] > 1:
28                count[nums[l_near]] -= 1
29                l_near += 1
30
31
32            if len(count) == k:
33                ans += l_near - l_far + 1
34
35        return ans