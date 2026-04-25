1class Solution:
2    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
3        ## convert them to numbers
4
5        nums = [ord(x) for x in letters]
6        target_num = ord(target)
7
8        for num in nums:
9            if num > target_num:
10                return chr(num)
11
12
13        ##print(nums)
14        return chr(nums[0])
15