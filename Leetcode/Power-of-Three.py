1class Solution:
2    def isPowerOfThree(self, n: int) -> bool:
3        ## solve using recursion
4
5        ## base recursion
6        if n == 1: # 1 is 3 power 0
7            return True
8        
9        if n <= 0 or n % 3 != 0: # invalid cases
10            return False
11
12        return self.isPowerOfThree(n // 3)
13