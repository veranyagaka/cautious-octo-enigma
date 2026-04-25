1class Solution(object):
2    def majorityElement(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        # Boyer–Moore algorithm 
8        # O(1) spance, O(n) time
9        candidate = None
10        count = 0
11        for num in nums:
12            if count == 0:
13                candidate = num
14            
15            if num == candidate:
16                count += 1
17
18            else:
19                count -= 1
20
21
22        return candidate
23
24        