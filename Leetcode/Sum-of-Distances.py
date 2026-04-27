1class Solution:
2    def distance(self, nums: List[int]) -> List[int]:
3        # O(n sqaured solution)
4        n = len(nums)
5        arr = [0] * n
6        hashmap = {} # storing value and the index
7        """
8        example:
9        nums = [1,3,1,1,2]
10        {
11            1: [0, 2, 3].
12            3: [1],
13            2: [4]
14        }
15
16        """
17        ## build the hashmap
18        for i, num in enumerate(nums):
19            if num not in hashmap:
20                hashmap[num] = []
21            hashmap[num].append(i)
22
23        ## print(hashmap)
24
25
26        for indices in hashmap.values():
27            k = len(indices)
28            if k == 1:
29                continue # a[i] is already 0
30                
31
32            ## i and j
33            prefix_sum = 0
34            for rank, idx in enumerate(indices):
35                arr[idx] += idx * rank - prefix_sum
36                prefix_sum += idx
37
38            suffix_sum = 0
39            for rank, idx in enumerate(reversed(indices)):
40                arr[idx] += suffix_sum - idx * rank
41                suffix_sum += idx
42
43        return arr