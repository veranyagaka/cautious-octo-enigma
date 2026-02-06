1class Solution:
2    def findDuplicates(self, nums: List[int]) -> List[int]:
3        hash_table = {}
4        ans = []
5        for num in nums:
6            if num in hash_table:
7                ans.append(num)
8                
9            hash_table[num] = 1
10        print(hash_table)
11        return ans
12