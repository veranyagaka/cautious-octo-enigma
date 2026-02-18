1class Solution:
2    def hasAlternatingBits(self, n: int) -> bool:
3        bin_no = bin(n)[2:]
4        
5        for i in range(len(bin_no) - 1):
6            if bin_no[i] == bin_no[i+1]:
7                return False
8
9        return True