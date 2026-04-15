1class Solution:
2    def isPowerOfFour(self, n: int) -> bool:
3
4        ## doing it recursively
5        if n == 1:
6            return True
7
8        if n <= 0 or n % 4 != 0:
9            return False
10
11     
12        return self.isPowerOfFour(n // 4)
13        