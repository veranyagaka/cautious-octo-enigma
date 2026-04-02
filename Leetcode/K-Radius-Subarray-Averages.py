1class Solution:
2    def getAverages(self, nums: List[int], k: int) -> List[int]:
3        
4        left = 0
5        n = len(nums)
6        running_sum = 0
7        div = (k * 2) + 1
8
9        res = [-1] * n
10
11        for r in range(n):
12            num = nums[r]
13            running_sum += num
14
15            # if (r - left + 1) < div: - dont need to do anythin
16            #     # res[] = -1
17            #     pass
18
19            if (r - left + 1) == div:
20                average = running_sum // div
21                center = r -k
22                res[center] = average
23                
24                running_sum -= nums[left]
25                left += 1
26
27        return res
28
29"""            
30if r < k or r >= n-k:
31
32"""