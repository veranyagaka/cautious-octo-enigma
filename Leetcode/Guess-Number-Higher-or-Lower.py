1# The guess API is already defined for you.
2# @param num, your guess
3# @return -1 if num is higher than the picked number
4#          1 if num is lower than the picked number
5#          otherwise return 0
6# def guess(num: int) -> int:
7
8class Solution:
9    def guessNumber(self, n: int) -> int:
10        low = 0
11        high = n
12
13        while low <= high:
14            mid = (low + high) // 2
15            x = guess(mid)
16            if x == 0:
17                return mid
18
19            elif x == -1:
20                high = mid -1
21
22            else:
23                low = mid + 1
24
25
26
27
28