1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        # two pointers
4        l,r = 0, len(numbers) - 1
5        
6        while l < r:
7            if numbers[l] + numbers[r] == target:
8                return [l+1, r+1]
9            elif numbers[l] + numbers[r] < target:
10                l += 1
11
12            else:
13                r -= 1
14
15        