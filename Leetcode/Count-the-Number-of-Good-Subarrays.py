1class Solution:
2    def countGood(self, nums: List[int], k: int) -> int:
3        good = 0
4        left = 0
5        n = len(nums)
6        freq = collections.Counter()
7
8        pairs = 0
9
10        # 
11        for right in range(n):
12
13            pairs += freq[nums[right]]
14            freq[nums[right]] += 1
15            
16            while pairs >= k: # shift the left
17                good += n - right
18                freq[nums[left]] -= 1
19                pairs -= freq[nums[left]]
20
21                if freq[nums[left]] == 0:
22                    del freq[nums[left]]
23                    
24                left += 1
25
26           
27
28
29        return good