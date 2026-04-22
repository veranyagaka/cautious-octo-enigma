1class Solution:
2    def mySqrt(self, x: int) -> int:
3
4        ## supposed to do a binary search
5        low = 0
6        high = x
7
8        while low <= high:
9            mid = (low + high) // 2
10            if mid * mid > x:
11                high = mid - 1
12
13            elif mid * mid < x:
14                low = mid + 1
15            else:
16                return mid
17
18        return high
19