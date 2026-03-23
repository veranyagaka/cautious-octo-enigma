1class Solution:
2    def leftRightDifference(self, nums: List[int]) -> List[int]:
3        leftSum = [0]
4        rightSum = [0]
5        l_run_sum, r_run_sum = 0, 0
6        n = len(nums)
7        ans = [0] * n
8
9        for i in range(n-1):
10            l_run_sum += nums[i]
11            leftSum.append(l_run_sum)
12
13        for i in range(n-1, 0, -1):
14            r_run_sum += nums[i]
15            rightSum.append(r_run_sum)
16
17        rightSum = rightSum[::-1]
18
19        for i in range(n):
20            ans[i] = abs(leftSum[i] - rightSum[i])
21
22        return ans