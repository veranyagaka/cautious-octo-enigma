1class Solution:
2    def findMaxAverage(self, nums: List[int], k: int) -> float:
3        max_sum, last_sum = sum(nums[:k]), sum(nums[:k])
4        n = len(nums)
5
6        l = 0
7        r = k
8
9        while r < n:
10            curr_sum = last_sum - nums[l] + nums[r]
11
12            max_sum = max(max_sum, curr_sum)
13
14            last_sum = curr_sum
15
16            l += 1
17            r += 1
18
19        ## moving windwo to right
20
21        return max_sum / k
22
23        