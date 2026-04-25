1class Solution:
2    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
3        ## convert them to numbers
4        ## letters is sorted
5        ## supposed to use binary search
6
7        nums = [ord(x) for x in letters]
8        target_num = ord(target)
9        low, high = 0, len(letters) - 1
10
11        while low <= high:
12            mid = (low + high) // 2
13
14            if nums[mid] > target_num:
15                ## how low can we go
16                high = mid - 1
17
18            else:
19                low = mid + 1
20
21        ## else we are returning the first chatacter in letters
22
23
24        if low == len(letters):
25            return chr(nums[0])
26        
27        return chr(nums[low])
28